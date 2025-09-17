#!/usr/bin/env python3
"""
Enhanced Laravel Benchmark Results Visualization Script

This script generates comprehensive visualizations from benchmark results,
including performance comparisons, resource utilization charts, and detailed analysis.

Requirements:
    pip install matplotlib seaborn pandas numpy

Usage:
    python3 visualize-results.py <results_directory> [output_directory]
"""

import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import logging

# Try to import visualization libraries
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import numpy as np
    VISUALIZATION_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Visualization libraries not available: {e}")
    print("Install with: pip install matplotlib seaborn pandas numpy")
    VISUALIZATION_AVAILABLE = False

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BenchmarkVisualizer:
    def __init__(self, results_dir, output_dir=None):
        self.results_dir = Path(results_dir)
        self.output_dir = Path(output_dir) if output_dir else self.results_dir / "charts"
        self.output_dir.mkdir(exist_ok=True)
        
        # Configure matplotlib for better output
        if VISUALIZATION_AVAILABLE:
            plt.style.use('seaborn-v0_8' if hasattr(plt.style, 'available') and 'seaborn-v0_8' in plt.style.available else 'default')
            sns.set_palette("husl")
    
    def load_benchmark_data(self):
        """Load all benchmark result files and organize data"""
        logger.info("Loading benchmark data from processed results...")
        
        processed_dir = self.results_dir / "processed"
        if not processed_dir.exists():
            logger.error(f"Processed results directory not found: {processed_dir}")
            return None
        
        benchmark_data = {}
        resource_data = {}
        
        # Load processed benchmark results
        for file_path in processed_dir.glob("benchmark-results-*.json"):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    config = data.get('benchmark_metadata', {}).get('config', 'unknown')
                    benchmark_data[config] = data
                    logger.info(f"Loaded benchmark data for: {config}")
            except Exception as e:
                logger.error(f"Error loading {file_path}: {e}")
        
        # Load resource monitoring data
        raw_dir = self.results_dir / "raw"
        if raw_dir.exists():
            for file_path in raw_dir.glob("resource-monitor-*.json"):
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        config = data.get('config', 'unknown')
                        resource_data[config] = data
                        logger.info(f"Loaded resource data for: {config}")
                except Exception as e:
                    logger.error(f"Error loading resource data {file_path}: {e}")
        
        return benchmark_data, resource_data
    
    def create_performance_comparison(self, benchmark_data):
        """Create performance comparison charts"""
        if not VISUALIZATION_AVAILABLE:
            logger.warning("Visualization libraries not available, skipping charts")
            return
        
        logger.info("Creating performance comparison charts...")
        
        # Extract metrics for comparison
        metrics = ['http_req_duration_avg_ms', 'http_req_duration_p95_ms', 'iteration_duration_avg_ms']
        configs = list(benchmark_data.keys())
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Laravel Benchmark Performance Comparison', fontsize=16, fontweight='bold')
        
        # Response time comparison
        ax1 = axes[0, 0]
        response_times = []
        config_names = []
        
        for config in configs:
            k6_metrics = benchmark_data[config].get('k6_summary_metrics', {})
            avg_time = float(str(k6_metrics.get('http_req_duration_avg_ms', 0)).replace('ms', ''))
            response_times.append(avg_time)
            config_names.append(config.replace('-', '\n'))
        
        bars1 = ax1.bar(config_names, response_times, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax1.set_title('Average Response Time (ms)', fontweight='bold')
        ax1.set_ylabel('Response Time (ms)')
        
        # Add value labels on bars
        for bar, value in zip(bars1, response_times):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(response_times)*0.01,
                    f'{value:.1f}ms', ha='center', va='bottom', fontweight='bold')
        
        # P95 Response time comparison
        ax2 = axes[0, 1]
        p95_times = []
        
        for config in configs:
            k6_metrics = benchmark_data[config].get('k6_summary_metrics', {})
            p95_time = float(str(k6_metrics.get('http_req_duration_p95_ms', 0)).replace('ms', ''))
            p95_times.append(p95_time)
        
        bars2 = ax2.bar(config_names, p95_times, color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
        ax2.set_title('95th Percentile Response Time (ms)', fontweight='bold')
        ax2.set_ylabel('P95 Response Time (ms)')
        
        for bar, value in zip(bars2, p95_times):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(p95_times)*0.01,
                    f'{value:.1f}ms', ha='center', va='bottom', fontweight='bold')
        
        # Performance improvement visualization
        ax3 = axes[1, 0]
        if len(response_times) >= 2:
            baseline = max(response_times)
            improvements = [(baseline - rt) / baseline * 100 for rt in response_times]
            colors = ['red' if imp < 0 else 'green' for imp in improvements]
            
            bars3 = ax3.bar(config_names, improvements, color=colors, alpha=0.7)
            ax3.set_title('Performance Improvement vs Worst Config (%)', fontweight='bold')
            ax3.set_ylabel('Improvement (%)')
            ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3)
            
            for bar, value in zip(bars3, improvements):
                ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (max(improvements) - min(improvements))*0.01,
                        f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Failure rate comparison
        ax4 = axes[1, 1]
        failure_rates = []
        
        for config in configs:
            k6_metrics = benchmark_data[config].get('k6_summary_metrics', {})
            failure_rate = float(str(k6_metrics.get('http_req_failed_rate', '0%')).replace('%', ''))
            failure_rates.append(failure_rate)
        
        bars4 = ax4.bar(config_names, failure_rates, color=['#FF6B6B', '#FFA07A', '#FFB347'])
        ax4.set_title('Request Failure Rate (%)', fontweight='bold')
        ax4.set_ylabel('Failure Rate (%)')
        
        for bar, value in zip(bars4, failure_rates):
            if value > 0:
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(failure_rates)*0.01,
                        f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'performance_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Performance comparison chart saved to: {self.output_dir / 'performance_comparison.png'}")
    
    def create_resource_utilization_charts(self, resource_data):
        """Create resource utilization charts"""
        if not VISUALIZATION_AVAILABLE or not resource_data:
            logger.warning("Cannot create resource charts - data or libraries unavailable")
            return
        
        logger.info("Creating resource utilization charts...")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Container Resource Utilization During Benchmarks', fontsize=16, fontweight='bold')
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
        
        for idx, (config, data) in enumerate(resource_data.items()):
            samples = data.get('samples', [])
            if not samples:
                continue
            
            # Extract time series data
            timestamps = [datetime.fromisoformat(s['timestamp'].replace('Z', '+00:00')) for s in samples]
            cpu_usage = [float(s['cpu_percent']) if s['cpu_percent'] != 'N/A' else 0 for s in samples]
            
            # Memory usage (extract numeric part)
            memory_usage = []
            for s in samples:
                mem_str = s['memory_usage']
                if 'MiB' in mem_str:
                    mem_value = float(mem_str.split(' ')[0])
                elif 'GiB' in mem_str:
                    mem_value = float(mem_str.split(' ')[0]) * 1024
                else:
                    mem_value = 0
                memory_usage.append(mem_value)
            
            color = colors[idx % len(colors)]
            
            # CPU utilization over time
            axes[0, 0].plot(timestamps, cpu_usage, label=config, color=color, linewidth=2)
            axes[0, 0].set_title('CPU Utilization Over Time', fontweight='bold')
            axes[0, 0].set_ylabel('CPU Usage (%)')
            axes[0, 0].legend()
            axes[0, 0].grid(True, alpha=0.3)
            
            # Memory utilization over time
            axes[0, 1].plot(timestamps, memory_usage, label=config, color=color, linewidth=2)
            axes[0, 1].set_title('Memory Utilization Over Time', fontweight='bold')
            axes[0, 1].set_ylabel('Memory Usage (MiB)')
            axes[0, 1].legend()
            axes[0, 1].grid(True, alpha=0.3)
        
        # Average resource usage comparison
        configs = list(resource_data.keys())
        avg_cpu = []
        avg_memory = []
        
        for config in configs:
            samples = resource_data[config].get('samples', [])
            if samples:
                cpu_values = [float(s['cpu_percent']) if s['cpu_percent'] != 'N/A' else 0 for s in samples]
                avg_cpu.append(np.mean(cpu_values))
                
                memory_values = []
                for s in samples:
                    mem_str = s['memory_usage']
                    if 'MiB' in mem_str:
                        mem_value = float(mem_str.split(' ')[0])
                    elif 'GiB' in mem_str:
                        mem_value = float(mem_str.split(' ')[0]) * 1024
                    else:
                        mem_value = 0
                    memory_values.append(mem_value)
                avg_memory.append(np.mean(memory_values))
            else:
                avg_cpu.append(0)
                avg_memory.append(0)
        
        # Average CPU usage bar chart
        config_names = [c.replace('-', '\n') for c in configs]
        bars1 = axes[1, 0].bar(config_names, avg_cpu, color=['#FF6B6B', '#4ECDC4'])
        axes[1, 0].set_title('Average CPU Usage (%)', fontweight='bold')
        axes[1, 0].set_ylabel('CPU Usage (%)')
        
        for bar, value in zip(bars1, avg_cpu):
            axes[1, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(avg_cpu)*0.01,
                           f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Average memory usage bar chart
        bars2 = axes[1, 1].bar(config_names, avg_memory, color=['#96CEB4', '#FFEAA7'])
        axes[1, 1].set_title('Average Memory Usage (MiB)', fontweight='bold')
        axes[1, 1].set_ylabel('Memory Usage (MiB)')
        
        for bar, value in zip(bars2, avg_memory):
            axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(avg_memory)*0.01,
                           f'{value:.0f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'resource_utilization.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Resource utilization chart saved to: {self.output_dir / 'resource_utilization.png'}")
    
    def create_detailed_analysis_chart(self, benchmark_data):
        """Create detailed benchmark analysis visualization"""
        if not VISUALIZATION_AVAILABLE:
            return
        
        logger.info("Creating detailed analysis chart...")
        
        # Extract Laravel-specific benchmark results
        laravel_metrics = {}
        
        for config, data in benchmark_data.items():
            custom_results = data.get('custom_benchmark_results', {})
            if 'scenarios' in custom_results:
                scenarios = custom_results['scenarios']
                laravel_metrics[config] = {
                    'cpu_intensive': scenarios.get('cpu_intensive', {}).get('avgDuration', 0),
                    'database_operations': scenarios.get('database_operations', {}).get('avgDuration', 0),
                    'cache_operations': scenarios.get('cache_operations', {}).get('avgDuration', 0),
                    'eloquent_operations': scenarios.get('eloquent_operations', {}).get('avgDuration', 0),
                    'laravel_features': scenarios.get('laravel_features', {}).get('avgDuration', 0)
                }
        
        if not laravel_metrics:
            logger.warning("No Laravel-specific metrics found for detailed analysis")
            return
        
        # Create radar chart for detailed comparison
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        fig.suptitle('Detailed Laravel Component Performance Analysis', fontsize=16, fontweight='bold')
        
        # Scenario performance comparison
        scenarios = ['CPU Intensive', 'Database Ops', 'Cache Ops', 'Eloquent Ops', 'Laravel Features']
        configs = list(laravel_metrics.keys())
        
        x = np.arange(len(scenarios))
        width = 0.35
        
        if len(configs) >= 2:
            config1_values = list(laravel_metrics[configs[0]].values())
            config2_values = list(laravel_metrics[configs[1]].values())
            
            bars1 = ax1.bar(x - width/2, config1_values, width, label=configs[0], alpha=0.8)
            bars2 = ax1.bar(x + width/2, config2_values, width, label=configs[1], alpha=0.8)
            
            ax1.set_title('Response Time by Laravel Component', fontweight='bold')
            ax1.set_ylabel('Average Response Time (ms)')
            ax1.set_xlabel('Test Scenarios')
            ax1.set_xticks(x)
            ax1.set_xticklabels(scenarios, rotation=45, ha='right')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Add value labels
            for bars in [bars1, bars2]:
                for bar in bars:
                    height = bar.get_height()
                    if height > 0:
                        ax1.text(bar.get_x() + bar.get_width()/2., height + max(config1_values + config2_values)*0.01,
                                f'{height:.1f}', ha='center', va='bottom', fontsize=10)
        
        # Performance improvement analysis
        if len(configs) >= 2:
            improvements = []
            scenario_names = []
            
            for scenario, config1_val in laravel_metrics[configs[0]].items():
                config2_val = laravel_metrics[configs[1]][scenario]
                if config1_val > 0 and config2_val > 0:
                    improvement = (config1_val - config2_val) / config1_val * 100
                    improvements.append(improvement)
                    scenario_names.append(scenario.replace('_', ' ').title())
            
            colors = ['green' if imp > 0 else 'red' for imp in improvements]
            bars = ax2.barh(scenario_names, improvements, color=colors, alpha=0.7)
            
            ax2.set_title(f'Performance Improvement:\n{configs[1]} vs {configs[0]}', fontweight='bold')
            ax2.set_xlabel('Improvement (%)')
            ax2.axvline(x=0, color='black', linestyle='-', alpha=0.3)
            ax2.grid(True, alpha=0.3)
            
            # Add value labels
            for bar, value in zip(bars, improvements):
                ax2.text(value + (max(improvements) - min(improvements))*0.01, bar.get_y() + bar.get_height()/2,
                        f'{value:.1f}%', ha='left' if value >= 0 else 'right', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'detailed_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Detailed analysis chart saved to: {self.output_dir / 'detailed_analysis.png'}")
    
    def generate_all_visualizations(self):
        """Generate all available visualizations"""
        logger.info("Starting comprehensive visualization generation...")
        
        benchmark_data, resource_data = self.load_benchmark_data()
        
        if not benchmark_data:
            logger.error("No benchmark data available for visualization")
            return False
        
        # Create various charts
        self.create_performance_comparison(benchmark_data)
        self.create_resource_utilization_charts(resource_data)
        self.create_detailed_analysis_chart(benchmark_data)
        
        # Create summary HTML report
        self.create_html_report(benchmark_data, resource_data)
        
        logger.info(f"All visualizations saved to: {self.output_dir}")
        return True
    
    def create_html_report(self, benchmark_data, resource_data):
        """Create an HTML report with embedded charts"""
        logger.info("Creating HTML report...")
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Laravel Benchmark Analysis Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; border-left: 4px solid #3498db; padding-left: 15px; }}
        .chart {{ text-align: center; margin: 30px 0; }}
        .chart img {{ max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px; }}
        .summary {{ background-color: #ecf0f1; padding: 20px; border-radius: 5px; margin: 20px 0; }}
        .metric {{ display: inline-block; margin: 10px 15px; padding: 10px; background-color: #3498db; color: white; border-radius: 5px; }}
        .timestamp {{ text-align: center; color: #7f8c8d; font-style: italic; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Laravel Benchmark Analysis Report</h1>
        <div class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
        
        <div class="summary">
            <h2>📊 Executive Summary</h2>
            <p>This report presents a comprehensive analysis of Laravel application performance across different configurations.</p>
            <div>
"""
        
        # Add configuration summary
        for config in benchmark_data.keys():
            html_content += f'<span class="metric">{config}</span>'
        
        html_content += """
            </div>
        </div>
        
        <h2>🔄 Performance Comparison</h2>
        <div class="chart">
            <img src="performance_comparison.png" alt="Performance Comparison Chart">
        </div>
        
        <h2>📈 Resource Utilization</h2>
        <div class="chart">
            <img src="resource_utilization.png" alt="Resource Utilization Chart">
        </div>
        
        <h2>🔍 Detailed Analysis</h2>
        <div class="chart">
            <img src="detailed_analysis.png" alt="Detailed Analysis Chart">
        </div>
        
        <div class="summary">
            <h2>💡 Key Insights</h2>
            <ul>
"""
        
        # Add insights based on data
        if len(benchmark_data) >= 2:
            configs = list(benchmark_data.keys())
            config1_metrics = benchmark_data[configs[0]].get('k6_summary_metrics', {})
            config2_metrics = benchmark_data[configs[1]].get('k6_summary_metrics', {})
            
            avg1 = float(str(config1_metrics.get('http_req_duration_avg_ms', 0)).replace('ms', ''))
            avg2 = float(str(config2_metrics.get('http_req_duration_avg_ms', 0)).replace('ms', ''))
            
            if avg1 > 0 and avg2 > 0:
                if avg2 < avg1:
                    improvement = (avg1 - avg2) / avg1 * 100
                    html_content += f"<li>{configs[1]} shows {improvement:.1f}% better response time than {configs[0]}</li>"
                else:
                    degradation = (avg2 - avg1) / avg1 * 100
                    html_content += f"<li>{configs[0]} performs {degradation:.1f}% better than {configs[1]}</li>"
        
        html_content += """
                <li>Resource utilization patterns indicate optimization opportunities</li>
                <li>Different Laravel components show varying performance characteristics</li>
                <li>OPcache configuration significantly impacts overall performance</li>
            </ul>
        </div>
        
        <div class="summary">
            <h2>🎯 Recommendations</h2>
            <ul>
                <li>Enable OPcache for production environments for optimal performance</li>
                <li>Monitor resource utilization to identify bottlenecks</li>
                <li>Consider caching strategies for database-heavy operations</li>
                <li>Regular performance testing should be part of the deployment pipeline</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
        
        with open(self.output_dir / 'benchmark_report.html', 'w') as f:
            f.write(html_content)
        
        logger.info(f"HTML report saved to: {self.output_dir / 'benchmark_report.html'}")

def main():
    parser = argparse.ArgumentParser(description='Generate visualizations from Laravel benchmark results')
    parser.add_argument('results_dir', help='Directory containing benchmark results')
    parser.add_argument('--output', '-o', help='Output directory for charts (default: results_dir/charts)')
    parser.add_argument('--format', choices=['png', 'pdf', 'svg'], default='png', help='Output format for charts')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.results_dir):
        logger.error(f"Results directory does not exist: {args.results_dir}")
        sys.exit(1)
    
    if not VISUALIZATION_AVAILABLE:
        logger.error("Visualization libraries not available. Install with: pip install matplotlib seaborn pandas numpy")
        sys.exit(1)
    
    visualizer = BenchmarkVisualizer(args.results_dir, args.output)
    
    if visualizer.generate_all_visualizations():
        print(f"\n✅ Visualizations generated successfully!")
        print(f"📁 Charts saved to: {visualizer.output_dir}")
        print(f"🌐 Open {visualizer.output_dir}/benchmark_report.html to view the complete report")
    else:
        print("\n❌ Failed to generate visualizations")
        sys.exit(1)

if __name__ == "__main__":
    main()
