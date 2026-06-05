# SQL & Excel Analytics Inventory

**Scan date:** June 5, 2026  
**Location:** `Master Portfolio Hub/SQL Portfolio/`

---

## File Inventory

| File | Type | Size | Status |
|------|------|------|--------|
| AI_Evaluator_And_Analytics_Combined_Workbook.xlsx | Excel | 36 KB | Active — full source |
| AI_Evaluator_And_Analytics_Combined_Workbook.xlsm.pdf | PDF export | 202 KB | Reference |
| Investment_App_Portfolio_Analysis_Workbook.xlsx | Excel | 76 KB | Active — full source |
| Investment_App_Portfolio_Analysis_Workbook.xlsm.pdf | PDF export | 363 KB | Reference |
| Quant_Analytics_Portfolio_Workbook.xlsx | Excel | 21 KB | Active — full source |
| Quant_Analytics_Portfolio_Workbook.xlsx.pdf | PDF export | 151 KB | Reference |
| Real_World_Data_Analytics_Portfolio_Workbook.xlsx | Excel | 32 KB | Active — full source |
| Real_World_Data_Analytics_Portfolio_Workbook.xlsx.pdf | PDF export | 190 KB | Reference |
| Actuarial_Analytics_Practice_Workbook.xlsx.pdf | PDF only | 346 KB | **Missing .xlsx source** |

---

## Workbook 1: AI Evaluator & Analytics Combined

### Sheets
| Sheet | Purpose | Records |
|-------|---------|---------|
| README | Workbook overview and portfolio explanation | — |
| Prompt_Rating_Practice | Direct evaluator tasks — rate 10 AI responses | 10 tasks |
| Pairwise_Evaluation | Compare Response A vs B with justification | 5 pairs |
| Evaluation_Data | Structured dataset for SQL/pivot/dashboard analysis | 150 rows |
| SQL_Practice | 11 SQL queries with solutions (Intermediate → Advanced) | 11 queries |
| Python_Practice | pandas equivalents for 6 analyses | 6 tasks |
| Dashboard | KPI formulas and category breakdown | Live KPIs |

### SQL Skills Demonstrated
- **Aggregations:** AVG, COUNT, GROUP BY, ORDER BY
- **Conditional logic:** CASE WHEN rate calculations
- **Filtering:** WHERE, IN, HAVING with multi-metric thresholds
- **Window functions:** RANK() OVER (PARTITION BY ... ORDER BY ...)
- **Subqueries:** Global average comparison, latency threshold
- **Time aggregation:** DATE_TRUNC monthly trends
- **Business reporting:** Hallucination rates, quality-to-cost ratios, evaluator bias, risk ranking

### Key Queries
1. Average overall rating by model
2. Hallucination rate by prompt category
3. Unsafe output count by model (Safety/Medical)
4. Rank models within prompt category (RANK window function)
5. Categories below 3.5 rating with >15% hallucination (HAVING)
6. Quality-to-cost ratio by model (NULLIF)
7. Evaluator strictness vs global average (subquery)
8. High latency + low quality filter (subquery)
9. Monthly model rating trend (DATE_TRUNC)
10. Writing-strong / reasoning-weak models (conditional HAVING)
11. Top 3 worst model/category by hallucination rate (HAVING + LIMIT)

### Dashboard KPIs
Total Evaluations, Average Overall Rating, Hallucination Count, Unsafe Output Count, Average Latency, Average Cost, Model comparison table, Category breakdown with hallucination rates

---

## Workbook 2: Investment App Portfolio Analysis

### Sheets
| Sheet | Purpose | Records |
|-------|---------|---------|
| README | Purpose, usage guide, app connection | — |
| Portfolio_Inputs | $200K allocation across 6 tickers | 6 holdings |
| Monthly_Returns | 24 months of ticker + portfolio returns | 24 rows |
| Risk_Metrics | Sharpe, volatility, drawdown per ticker | 6 tickers |
| Correlation_Data | 6×6 correlation matrix | 36 cells |
| Monte_Carlo_Scenarios | 500 simulation ending values | 500 rows |
| Optimizer_Portfolios | 251 candidate allocations | 251 rows |
| Pivot_Practice | 10 pivot table exercises | 10 exercises |
| SQL_Practice | 11 SQL queries with solutions | 11 queries |
| Dashboard_Tasks | 9 chart/table storytelling tasks | 9 tasks |
| Dashboard | Live KPI dashboard with chart recommendations | Built |

### SQL Skills Demonstrated
- **Aggregations:** AVG, COUNT, GROUP BY
- **Subqueries:** Portfolio volatility threshold, current Sharpe comparison
- **Conditional logic:** CASE WHEN bucketing, positive/negative month counts
- **Filtering:** WHERE excess return > 0, LIMIT worst 5
- **Business reporting:** Downside probability, percentile buckets, efficient frontier candidates

### Pivot Exercises (10)
1. Capital split by asset class (SUM allocation)
2. Best risk-adjusted performance by asset type (AVG Sharpe)
3. Riskiest holdings (MAX volatility)
4. Portfolio vs SPY monthly returns
5. Months outperforming benchmark (AVG excess return)
6. Monte Carlo outcome distribution (COUNT by bucket)
7. Optimizer portfolios vs current (return, vol, Sharpe)
8. Highest Sharpe allocation (MAX Sharpe)
9. Risk-return comparison table
10. Negative return month frequency (COUNT)

### Dashboard Tasks (9)
Allocation chart, return vs SPY line, risk-return scatter, Sharpe bar chart, correlation heatmap, Monte Carlo histogram, efficient frontier scatter, recommended allocation table, executive summary

---

## Workbook 3: Quant Analytics Portfolio

### Sheets
| Sheet | Purpose | Records |
|-------|---------|---------|
| Claims_Data | Insurance claims with policy type, state, risk level | 150 rows |
| Baseball_Analytics | Player stats — HR, AVG, OBP, OPS, salary | 60 rows |
| Statistical_Modeling | Distribution reference (Normal, Poisson, Gamma, etc.) | 6 distributions |
| SQL_Practice | 10 practice questions (no solutions in workbook) | 10 questions |
| Pivot_Practice | 8 pivot exercises | 8 exercises |
| Dashboard_Ideas | 9 KPI suggestions | 9 KPIs |

### SQL Practice Questions
1. Average claim amount by policy type
2. Top 5 largest claims
3. Highest OPS by team
4. Average salary by age group
5. Open claims with reserve > claim amount
6. Monthly claim trend
7. Average HR by team
8. Highest-risk states by total claims
9. OPS vs Salary correlation-style analysis
10. Count denied claims by state

### Pivot Exercises (8)
1. Total claim amount by policy type
2. Average claim by risk level
3. Claims by state and status (cross-tab)
4. Average OPS by team
5. Highest salary by team
6. HR totals by age group
7. Average premium by state
8. Claim severity range by policy type

---

## Workbook 4: Real World Data Analytics

### Sheets
| Sheet | Purpose | Records |
|-------|---------|---------|
| Credit_Risk_Data | Company financial ratios + credit score + default flag | 200 rows |
| Portfolio_Returns | Monthly returns, volatility, Sharpe, drawdown | 24 rows |
| Insurance_Claims | Claims with fraud flags, severity buckets, regions | 300 rows |
| Distribution_Practice | 6 distributions with business use cases | 6 types |
| SQL_Analytics_Tasks | 10 practice questions | 10 questions |
| Dashboard_Ideas | 10 dashboard components | 10 KPIs |
| Portfolio_Project_Ideas | 6 project concepts | 6 ideas |

### SQL Analytics Tasks
1. Average claim amount by policy type
2. Top 10 companies by debt ratio
3. Default rate by sector
4. Months with Sharpe ratio above 1
5. Fraud claims by region
6. Highest drawdown month
7. Correlation between volatility and returns
8. Sectors with default rates above average
9. Rank portfolios by risk-adjusted return (window function)
10. Average severity by region

### Dashboard Components
Default rate KPI, claim severity, fraud detection rate, portfolio return trend, Sharpe dashboard, volatility vs return scatter, claim frequency heatmap, sector risk ranking, credit score distribution, risk exposure dashboard

---

## Workbook 5: Actuarial Analytics Practice (PDF Only)

- **Status:** PDF export exists (346 KB) but `.xlsx` source is missing from portfolio folder
- **Action needed:** Restore Excel source file for full portfolio integration
- **Domain:** Actuarial science, insurance analytics, loss reserving

---

## Combined Skills Inventory

### SQL Skills Matrix

| Skill | Workbooks | Example Techniques |
|-------|-----------|-------------------|
| SELECT / FROM | All | Basic retrieval |
| WHERE filtering | All | Category, date, threshold filters |
| GROUP BY + aggregations | All | AVG, COUNT, SUM, MIN, MAX |
| HAVING | AI Evaluator, Investment | Multi-metric thresholds |
| CASE WHEN | All | Rate calculations, bucketing |
| Subqueries | AI Evaluator, Investment | Threshold comparisons, benchmarks |
| Window functions | AI Evaluator, Real World | RANK() OVER, PARTITION BY |
| ORDER BY + LIMIT | All | Top-N, worst-N rankings |
| DATE_TRUNC | AI Evaluator | Monthly trend aggregation |
| NULLIF | AI Evaluator | Division safety in cost analysis |
| IN clause | AI Evaluator | Category filtering |
| Conditional aggregation | AI Evaluator | Writing vs reasoning performance |

### Excel Skills Matrix

| Skill | Workbooks | Count |
|-------|-----------|-------|
| Pivot tables | Investment, Quant | 18 exercises |
| Dashboard KPIs | All 4 active workbooks | 30+ KPIs |
| Financial modeling | Investment | Sharpe, Monte Carlo, frontier |
| Distribution practice | Quant, Real World | 12 distribution types |
| Data tables | All | 900+ total records |
| Chart storytelling | Investment | 9 dashboard tasks |
| Cross-tab analysis | Quant | State × status pivot |
| Correlation analysis | Investment, Quant | Matrix + OPS/salary |
| Executive summaries | Investment | Analyst recommendation template |

---

## Total Portfolio Metrics

| Metric | Count |
|--------|-------|
| Active Excel workbooks | 4 |
| Total data records | ~1,400+ |
| SQL queries with solutions | 22 |
| SQL practice questions | 20 |
| Pivot table exercises | 18 |
| Dashboard KPIs/components | 30+ |
| Distribution types practiced | 12 |
| Business domains covered | 6 (AI eval, finance, insurance, credit, sports, actuarial) |
