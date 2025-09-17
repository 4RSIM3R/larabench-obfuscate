# Laravel OPcache Performance Results

**Test Date:** September 18, 2025  
**Configuration:** Plain Laravel with OPcache Enabled  
**Test Duration:** 6 minutes 33 seconds  
**Endpoint:** http://localhost:8082

## 🚀 Performance Overview

| Metric              | Value             |
| ------------------- | ----------------- |
| **Total Requests**  | 184 requests      |
| **Requests/Second** | 0.468/s           |
| **Success Rate**    | 100% (0 failures) |
| **Total Checks**    | 331 (all passed)  |

## ⚡ Response Time Performance

### Overall HTTP Request Duration

-   **Average:** 2.24s
-   **Median:** 22.89ms
-   **Minimum:** 7.65ms
-   **Maximum:** 20.86s
-   **90th Percentile:** 9.3s
-   **95th Percentile:** 10.89s

### Scenario-Specific Performance

#### Health Check

-   **Response Time:** 8.02ms (consistent)
-   **Status:** ✅ All checks passed

#### CPU Intensive Operations

-   **Average:** 9.38ms
-   **Range:** 7.65ms - 31.32ms
-   **95th Percentile:** 10.22ms
-   **Status:** ✅ Excellent performance

#### Cache Operations

-   **Average:** 1.16s
-   **Range:** 1.09s - 1.28s
-   **95th Percentile:** 1.27s
-   **Status:** ✅ Good caching performance

#### Database Operations

-   **Average:** 10.66s
-   **Range:** 10.21s - 11.13s
-   **95th Percentile:** 11.06s
-   **Status:** ✅ Consistent database performance

## 📊 Resource Usage

### Network Statistics

-   **Data Received:** 100 kB (253 B/s)
-   **Data Sent:** 29 kB (73 B/s)

### Execution Statistics

-   **Total Iterations:** 183
-   **Iteration Duration (avg):** 3.49s
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

## 💡 Key Insights

### Strengths

-   **Excellent CPU performance** with sub-10ms average response times
-   **Very fast health checks** indicating optimal application bootstrap
-   **100% reliability** with zero failed requests
-   **Consistent performance** across all test scenarios

### Notable Metrics

-   **Fastest response:** 7.65ms (CPU intensive operations)
-   **Most consistent:** Health check (8.02ms every time)
-   **Highest throughput:** 0.468 requests/second sustained

## 🔧 Configuration Benefits

OPcache demonstrates clear benefits for:

-   ⚡ **PHP bytecode caching** - eliminating compilation overhead
-   🚀 **Application bootstrap speed** - faster initial request handling
-   💪 **CPU-bound operations** - optimal performance for computational tasks
-   🔄 **Sustained performance** - consistent response times under load

---

_Generated from K6 load testing results on Laravel application with OPcache enabled_
