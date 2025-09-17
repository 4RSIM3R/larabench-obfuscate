# Laravel Performance Comparison: OPcache vs No-OPcache

**Test Date:** September 18, 2025  
**Test Duration:** ~6.5 minutes per configuration  
**Laravel Application Benchmark Analysis**

## 🏆 Executive Summary

OPcache provides **significant performance improvements** across all PHP-intensive operations, with the most dramatic gains in CPU-bound tasks and application bootstrap performance. Database operations show minimal improvement as expected, since they are I/O-bound rather than CPU-bound.

## 📊 Head-to-Head Performance Comparison

### Overall Request Performance

| Metric                    | No OPcache | OPcache | Improvement | Performance Gain            |
| ------------------------- | ---------- | ------- | ----------- | --------------------------- |
| **Average Response Time** | 2.55s      | 2.24s   | -0.31s      | **12.2% faster** ⚡         |
| **Median Response Time**  | 65.84ms    | 22.89ms | -42.95ms    | **65.2% faster** 🚀         |
| **95th Percentile**       | 11.88s     | 10.89s  | -0.99s      | **8.3% faster**             |
| **Maximum Response Time** | 23.85s     | 20.86s  | -2.99s      | **12.5% faster**            |
| **Total Requests**        | 170        | 184     | +14         | **8.2% more throughput** 📈 |
| **Requests/Second**       | 0.433/s    | 0.468/s | +0.035/s    | **8.1% higher rate**        |

## 🎯 Scenario-by-Scenario Analysis

### 1. Health Check Performance

| Configuration | Response Time | Improvement         |
| ------------- | ------------- | ------------------- |
| No OPcache    | 48.57ms       | -                   |
| **OPcache**   | **8.02ms**    | **🏆 83.5% faster** |

_The health check represents application bootstrap performance - OPcache dramatically reduces startup overhead._

### 2. CPU Intensive Operations

| Configuration | Average    | 95th Percentile | Improvement                 |
| ------------- | ---------- | --------------- | --------------------------- |
| No OPcache    | 50.89ms    | 59.73ms         | -                           |
| **OPcache**   | **9.38ms** | **10.22ms**     | **🏆 81.6% / 82.9% faster** |

_CPU-bound operations see the largest gains as OPcache eliminates PHP compilation overhead._

### 3. Cache Operations

| Configuration | Average   | 95th Percentile | Improvement                |
| ------------- | --------- | --------------- | -------------------------- |
| No OPcache    | 1.25s     | 1.43s           | -                          |
| **OPcache**   | **1.16s** | **1.27s**       | **✅ 7.2% / 11.2% faster** |

_Moderate improvement in cache operations due to reduced PHP processing overhead._

### 4. Database Operations

| Configuration | Average | 95th Percentile | Improvement      |
| ------------- | ------- | --------------- | ---------------- |
| No OPcache    | 10.65s  | 11.14s          | -                |
| OPcache       | 10.66s  | 11.06s          | **≈ Negligible** |

_Database operations show minimal difference as they are I/O-bound, not CPU-bound._

## 📈 Resource Utilization Comparison

### Network & Processing

| Metric                       | No OPcache      | OPcache          | Difference      |
| ---------------------------- | --------------- | ---------------- | --------------- |
| **Data Received**            | 93 kB (237 B/s) | 100 kB (253 B/s) | +7 kB           |
| **Data Sent**                | 27 kB (68 B/s)  | 29 kB (73 B/s)   | +2 kB           |
| **Total Iterations**         | 169             | 183              | +14 iterations  |
| **Iteration Duration (avg)** | 3.8s            | 3.49s            | **8.2% faster** |

## 🔍 Performance Impact Analysis

### 🥇 Dramatic Improvements (70%+ faster)

-   **Health Check:** 83.5% improvement
-   **CPU Intensive Operations:** 81.6% improvement

### ✅ Moderate Improvements (5-15% faster)

-   **Overall Average Response:** 12.2% improvement
-   **Cache Operations:** 7-11% improvement
-   **Total Throughput:** 8.2% improvement

### ➖ Minimal Impact

-   **Database Operations:** No significant change (expected)

## 💡 Key Insights & Recommendations

### 🎯 Why OPcache Works

1. **Eliminates PHP compilation** on every request
2. **Reduces CPU overhead** for bytecode parsing
3. **Faster application bootstrap** and initialization
4. **Improved memory efficiency** through bytecode caching

### 📊 Business Impact

-   **65% faster median response times** = Better user experience
-   **8% higher throughput** = More requests handled with same resources
-   **83% faster health checks** = Faster deployment and monitoring
-   **100% reliability maintained** = No trade-offs in stability

### 🚀 Production Recommendations

#### ✅ **STRONGLY RECOMMENDED: Enable OPcache**

-   **Immediate performance gains** with zero code changes
-   **Significant improvement** in user-facing response times
-   **Better resource utilization** and cost efficiency
-   **No negative side effects** observed

#### 🎯 **Expected Benefits in Production**

-   **Faster page loads** especially for PHP-heavy operations
-   **Reduced server CPU usage** per request
-   **Better scalability** under load
-   **Improved cost efficiency** in cloud environments

#### ⚙️ **Configuration Considerations**

-   Monitor OPcache memory usage in production
-   Implement proper cache invalidation for deployments
-   Consider OPcache preloading for further optimization

## 📋 Test Environment Details

### Test Configuration

-   **Scenarios:** 8 different load patterns
-   **Max Virtual Users:** 6 concurrent users
-   **Test Types:** Health check, CPU intensive, cache ops, database ops, stress tests
-   **Success Rate:** 100% for both configurations
-   **Reliability:** Zero failed requests in either test

### Measurement Methodology

-   **K6 Load Testing** with comprehensive scenarios
-   **Real HTTP requests** to actual Laravel endpoints
-   **Multiple performance dimensions** measured simultaneously
-   **Statistical analysis** including percentiles and distributions

---

## 🏁 Conclusion

**OPcache delivers substantial performance improvements** for this Laravel application, particularly excelling in CPU-bound operations while maintaining perfect reliability. The **65% improvement in median response times** and **8% increase in throughput** make OPcache an essential optimization for production deployment.

**Bottom Line:** Enable OPcache in production - the performance gains are significant with no observed downsides.

---

_Comprehensive analysis based on K6 load testing results comparing Laravel with and without OPcache optimization_
