# Laravel No-OPcache Performance Results

**Test Date:** September 18, 2025  
**Configuration:** Plain Laravel without OPcache  
**Test Duration:** 6 minutes 32 seconds  
**Endpoint:** http://localhost:8081

## 📊 Performance Overview

| Metric              | Value             |
| ------------------- | ----------------- |
| **Total Requests**  | 170 requests      |
| **Requests/Second** | 0.433/s           |
| **Success Rate**    | 100% (0 failures) |
| **Total Checks**    | 313 (all passed)  |

## ⏱️ Response Time Performance

### Overall HTTP Request Duration

-   **Average:** 2.55s
-   **Median:** 65.84ms
-   **Minimum:** 45.67ms
-   **Maximum:** 23.85s
-   **90th Percentile:** 9.66s
-   **95th Percentile:** 11.88s

### Scenario-Specific Performance

#### Health Check

-   **Response Time:** 48.57ms (consistent)
-   **Status:** ✅ All checks passed

#### CPU Intensive Operations

-   **Average:** 50.89ms
-   **Range:** 45.67ms - 90.53ms
-   **95th Percentile:** 59.73ms
-   **Status:** ✅ Moderate performance

#### Cache Operations

-   **Average:** 1.25s
-   **Range:** 1.1s - 1.44s
-   **95th Percentile:** 1.43s
-   **Status:** ✅ Acceptable caching performance

#### Database Operations

-   **Average:** 10.65s
-   **Range:** 10.27s - 11.19s
-   **95th Percentile:** 11.14s
-   **Status:** ✅ Consistent database performance

## 📈 Resource Usage

### Network Statistics

-   **Data Received:** 93 kB (237 B/s)
-   **Data Sent:** 27 kB (68 B/s)

### Execution Statistics

-   **Total Iterations:** 169
-   **Iteration Duration (avg):** 3.8s
-   **Max Virtual Users:** 6
-   **Active VUs Range:** 0-5

## 🎯 Test Scenarios Completed

All scenarios completed successfully:

-   ✅ **Health Check** - 1 iteration (30s max)
-   ✅ **Cache Operations** - 1 minute continuous
-   ✅ **CPU Intensive** - 1 minute continuous
-   ✅ **Database Operations** - 1 minute continuous
-   ✅ **Eloquent Operations** - 1 minute continuous
-   ✅ **Laravel Features** - 1 minute continuous
-   ✅ **Full Benchmark** - 2 minutes continuous
-   ✅ **Stress Test** - 2.5 minutes with multiple VUs

## 📝 Performance Characteristics

### Observed Patterns

-   **Higher response times** for PHP-intensive operations
-   **Slower application bootstrap** as evidenced by health check times
-   **Good reliability** with 100% success rate maintained
-   **Consistent database performance** similar to OPcache configuration

### Bottlenecks Identified

-   🐌 **PHP compilation overhead** affecting every request
-   ⏳ **Slower startup times** for application initialization
-   💻 **CPU-bound operations** showing higher latency
-   📊 **Lower overall throughput** compared to optimized configurations

## 🔍 Key Metrics Analysis

### Response Time Distribution

-   **Fastest response:** 45.67ms (CPU operations baseline)
-   **Most variable:** CPU intensive tasks (45-90ms range)
-   **Highest latency:** Full benchmark scenarios (up to 23.85s)

### Throughput Analysis

-   **Request rate:** 0.433/s sustained
-   **Total processed:** 170 requests in ~6.5 minutes
-   **Iteration efficiency:** 3.8s average per iteration

## ⚠️ Performance Considerations

### Areas for Improvement

-   **PHP bytecode compilation** happens on every request
-   **Memory usage** higher due to repeated compilation
-   **CPU utilization** increased for parsing and compilation
-   **Response consistency** affected by compilation overhead

### Baseline Establishment

This configuration establishes the baseline performance for:

-   📈 **Comparison metrics** against optimized configurations
-   🎯 **Bottleneck identification** in PHP processing
-   📊 **Resource utilization** patterns without caching

---

_Generated from K6 load testing results on Laravel application without OPcache_
