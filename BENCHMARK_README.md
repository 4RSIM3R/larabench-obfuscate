# Enhanced Laravel Benchmark Suite

This enhanced benchmark suite provides comprehensive performance analysis for Laravel applications across different configurations, with advanced result collection, visualization, and comparative analysis capabilities.

## 🚀 Features

### Enhanced Data Collection

-   **Comprehensive Metrics**: Collects K6 performance metrics, container resource utilization, and Laravel-specific benchmark results
-   **Real-time Monitoring**: Tracks CPU, memory, network, and disk I/O during benchmark execution
-   **Structured Results**: Organizes results in JSON format for easy analysis and processing
-   **System Information**: Captures host system details for reproducible benchmarking

### Advanced Analysis

-   **Performance Comparison**: Automatically compares multiple configurations
-   **Statistical Analysis**: Calculates performance improvements, standard deviations, and percentile metrics
-   **Resource Analysis**: Analyzes container performance and resource efficiency
-   **Failure Analysis**: Tracks and reports request failures and errors

### Visualization & Reporting

-   **Interactive Charts**: Generates performance comparison, resource utilization, and detailed analysis charts
-   **HTML Reports**: Creates comprehensive HTML reports with embedded visualizations
-   **Markdown Summaries**: Provides structured markdown reports for documentation
-   **Comparative Analysis**: Highlights performance differences between configurations

## 📁 Directory Structure

```
benchmark-results/
├── raw/                    # Raw K6 output and monitoring data
│   ├── k6-raw-*.json      # Raw K6 benchmark data
│   ├── resource-monitor-*.json  # Container resource monitoring
│   └── health-check-*.json     # Health check results
├── processed/              # Processed benchmark results
│   └── benchmark-results-*.json  # Comprehensive analysis results
├── logs/                   # Detailed logs and outputs
│   ├── benchmark-*.log     # Main benchmark execution log
│   ├── k6-output-*.log     # K6 detailed output
│   └── container-logs-*.log    # Container logs
├── charts/                 # Generated visualizations
│   ├── performance_comparison.png
│   ├── resource_utilization.png
│   ├── detailed_analysis.png
│   └── benchmark_report.html
├── system-info-*.json      # System information
├── benchmark-summary-*.json    # Comprehensive analysis
└── comparative-analysis-*.md   # Markdown report
```

## 🛠 Prerequisites

### Required Software

-   **Docker**: For containerized Laravel environments
-   **K6**: Load testing tool (`brew install k6` or visit [k6.io](https://k6.io))
-   **Python 3**: For analysis and visualization
-   **Bash**: For the main benchmark script

### Optional Dependencies (for visualization)

```bash
pip install matplotlib seaborn pandas numpy
```

## 📊 Usage

### Basic Benchmark Execution

```bash
# Run the enhanced benchmark suite
./run-benchmarks.sh

# The script will automatically:
# 1. Collect system information
# 2. Build Docker images for different configurations
# 3. Execute comprehensive benchmarks
# 4. Generate analysis and reports
```

### Visualization Generation

```bash
# Generate visualizations from results
./visualize-results.py ./benchmark-results

# Or specify custom output directory
./visualize-results.py ./benchmark-results --output ./custom-charts
```

### Manual Analysis

```bash
# View the comprehensive analysis
cat benchmark-results/benchmark-summary-*.json

# Read the markdown report
cat benchmark-results/comparative-analysis-*.md

# Open the HTML report
open benchmark-results/charts/benchmark_report.html
```

## 🔧 Configuration

### Benchmark Configurations

The suite tests the following Laravel configurations:

1. **Plain Laravel (No OPcache)**: `plain-no-opcache`

    - Standard Laravel installation
    - OPcache disabled
    - Baseline performance measurement

2. **Plain Laravel (OPcache)**: `plain-opcache`
    - Standard Laravel installation
    - OPcache enabled and optimized
    - Performance optimization measurement

### Test Scenarios

Each configuration is tested against multiple scenarios:

-   **Health Check**: Basic connectivity and responsiveness
-   **CPU Intensive**: Computational workload testing
-   **Database Operations**: Database query and transaction performance
-   **Cache Operations**: Caching system performance
-   **Eloquent Operations**: ORM performance testing
-   **Laravel Features**: Framework-specific functionality testing
-   **Full Benchmark**: Comprehensive application testing
-   **Stress Test**: Load testing with varying user counts

### Resource Monitoring

Real-time monitoring captures:

-   CPU utilization percentage
-   Memory usage (RSS and cache)
-   Network I/O statistics
-   Block I/O operations
-   Container lifecycle metrics

## 📈 Metrics Collected

### K6 Performance Metrics

-   **Response Time**: Average, median, 95th percentile
-   **Throughput**: Requests per second
-   **Success Rate**: Percentage of successful requests
-   **Resource Timing**: Connect time, transfer time, etc.

### Container Resource Metrics

-   **CPU Usage**: Real-time CPU utilization
-   **Memory Usage**: RSS memory consumption
-   **Network I/O**: Ingress/egress traffic
-   **Disk I/O**: Read/write operations

### Laravel Application Metrics

-   **Execution Time**: Per test scenario
-   **Memory Consumption**: Peak usage per test
-   **Database Queries**: Query count and timing
-   **Cache Performance**: Hit rates and response times

## 🔍 Analysis Features

### Performance Comparison

-   Side-by-side configuration comparison
-   Performance improvement calculations
-   Statistical significance testing
-   Bottleneck identification

### Resource Efficiency Analysis

-   Resource utilization trends
-   Efficiency ratios (performance per resource unit)
-   Scalability indicators
-   Optimization recommendations

### Failure Analysis

-   Error rate tracking
-   Failure pattern identification
-   Timeout analysis
-   Recovery time measurement

## 📊 Visualization Types

### Performance Comparison Charts

-   Response time comparison
-   Throughput comparison
-   Success rate visualization
-   Performance improvement analysis

### Resource Utilization Charts

-   CPU usage over time
-   Memory consumption trends
-   Resource efficiency comparison
-   Peak usage analysis

### Detailed Analysis Charts

-   Laravel component performance
-   Scenario-specific analysis
-   Optimization opportunity identification
-   Performance regression detection

## 🚨 Troubleshooting

### Common Issues

1. **K6 Not Found**

    ```bash
    # Install K6
    brew install k6
    # Or download from https://k6.io
    ```

2. **Docker Issues**

    ```bash
    # Ensure Docker is running
    docker ps

    # Clean up if needed
    docker system prune
    ```

3. **Permission Issues**

    ```bash
    # Make scripts executable
    chmod +x run-benchmarks.sh
    chmod +x visualize-results.py
    ```

4. **Python Dependencies**
    ```bash
    # Install visualization dependencies
    pip install matplotlib seaborn pandas numpy
    ```

### Log Analysis

Check the logs for detailed information:

```bash
# Main execution log
tail -f benchmark-results/logs/benchmark-*.log

# K6 detailed output
cat benchmark-results/logs/k6-output-*.log

# Container logs
cat benchmark-results/logs/container-logs-*.log
```

## 🎯 Best Practices

### Before Running Benchmarks

1. Ensure system is not under load
2. Close unnecessary applications
3. Use consistent hardware configurations
4. Run multiple iterations for statistical significance

### During Benchmarks

1. Monitor system resources
2. Avoid interrupting the process
3. Ensure stable network connectivity
4. Monitor container health

### After Benchmarks

1. Review all generated reports
2. Compare results across runs
3. Identify performance patterns
4. Document findings and recommendations

## 🔮 Future Enhancements

### Planned Features

-   [ ] Additional Laravel configurations (Queue workers, Horizon)
-   [ ] Database performance profiling
-   [ ] CDN and caching layer testing
-   [ ] Multi-region benchmark execution
-   [ ] Automated performance regression detection
-   [ ] Integration with CI/CD pipelines
-   [ ] Real-time dashboard for live monitoring
-   [ ] Historical performance tracking

### Customization Options

-   [ ] Custom test scenarios
-   [ ] Configurable resource limits
-   [ ] Custom metrics collection
-   [ ] Integration with monitoring systems
-   [ ] Export to external analytics platforms

## 📚 Additional Resources

-   [K6 Documentation](https://k6.io/docs/)
-   [Laravel Performance Optimization](https://laravel.com/docs/optimization)
-   [Docker Best Practices](https://docs.docker.com/develop/best-practices/)
-   [OPcache Configuration](https://www.php.net/manual/en/opcache.configuration.php)

## 🤝 Contributing

To contribute improvements to this benchmark suite:

1. Fork the repository
2. Create a feature branch
3. Implement your enhancement
4. Add tests and documentation
5. Submit a pull request

## 📄 License

This enhanced benchmark suite is provided as-is for performance analysis and optimization purposes.
