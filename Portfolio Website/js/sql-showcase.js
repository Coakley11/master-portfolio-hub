const SQL_QUERIES = [
  {
    workbook: "AI Evaluator & Analytics",
    difficulty: "intermediate",
    title: "Average overall rating by model",
    concepts: "GROUP BY, AVG, ORDER BY",
    sql: `SELECT model_name, AVG(overall_rating) AS avg_rating
FROM evaluation_data
GROUP BY model_name
ORDER BY avg_rating DESC;`
  },
  {
    workbook: "AI Evaluator & Analytics",
    difficulty: "intermediate",
    title: "Hallucination rate by prompt category",
    concepts: "CASE WHEN, conditional aggregation, rate calculation",
    sql: `SELECT prompt_category,
       AVG(CASE WHEN hallucination_flag = 'Yes' THEN 1.0 ELSE 0 END) AS hallucination_rate
FROM evaluation_data
GROUP BY prompt_category
ORDER BY hallucination_rate DESC;`
  },
  {
    workbook: "AI Evaluator & Analytics",
    difficulty: "hard",
    title: "Rank models within each prompt category",
    concepts: "Window function, RANK(), PARTITION BY",
    sql: `SELECT prompt_category, model_name,
       AVG(overall_rating) AS avg_rating,
       RANK() OVER (PARTITION BY prompt_category
                    ORDER BY AVG(overall_rating) DESC) AS category_rank
FROM evaluation_data
GROUP BY prompt_category, model_name;`
  },
  {
    workbook: "AI Evaluator & Analytics",
    difficulty: "hard",
    title: "Categories below quality threshold with high hallucination",
    concepts: "HAVING, conditional aggregation, multi-metric filter",
    sql: `SELECT prompt_category,
       AVG(overall_rating) AS avg_rating,
       AVG(CASE WHEN hallucination_flag='Yes' THEN 1.0 ELSE 0 END) AS hallucination_rate
FROM evaluation_data
GROUP BY prompt_category
HAVING AVG(overall_rating) < 3.5
   AND AVG(CASE WHEN hallucination_flag='Yes' THEN 1.0 ELSE 0 END) > 0.15;`
  },
  {
    workbook: "AI Evaluator & Analytics",
    difficulty: "advanced",
    title: "Monthly model rating trend",
    concepts: "DATE_TRUNC, time aggregation, GROUP BY",
    sql: `SELECT DATE_TRUNC('month', date) AS month, model_name,
       AVG(overall_rating) AS avg_rating
FROM evaluation_data
GROUP BY month, model_name
ORDER BY month, model_name;`
  },
  {
    workbook: "Investment Portfolio Analysis",
    difficulty: "intermediate",
    title: "Average annual return by asset type",
    concepts: "GROUP BY, AVG, ORDER BY",
    sql: `SELECT asset_type, AVG(annual_return) AS avg_return
FROM risk_metrics
GROUP BY asset_type
ORDER BY avg_return DESC;`
  },
  {
    workbook: "Investment Portfolio Analysis",
    difficulty: "intermediate",
    title: "Holdings riskier than portfolio volatility",
    concepts: "Subquery, WHERE filter",
    sql: `SELECT ticker, annual_volatility
FROM risk_metrics
WHERE annual_volatility > (
  SELECT portfolio_annual_volatility FROM portfolio_summary
);`
  },
  {
    workbook: "Investment Portfolio Analysis",
    difficulty: "intermediate",
    title: "Monte Carlo downside probability",
    concepts: "CASE WHEN, AVG, probability calculation",
    sql: `SELECT AVG(CASE WHEN ending_value_10y < 200000 THEN 1.0 ELSE 0 END) AS prob_loss
FROM monte_carlo_scenarios;`
  },
  {
    workbook: "Investment Portfolio Analysis",
    difficulty: "hard",
    title: "Monte Carlo percentile buckets",
    concepts: "CASE WHEN bucketing, COUNT, GROUP BY",
    sql: `SELECT CASE
         WHEN ending_value_10y < 250000 THEN '<250k'
         WHEN ending_value_10y < 400000 THEN '250k-400k'
         ELSE '400k+'
       END AS bucket,
       COUNT(*) AS simulations
FROM monte_carlo_scenarios
GROUP BY bucket;`
  },
  {
    workbook: "Investment Portfolio Analysis",
    difficulty: "hard",
    title: "Optimizer portfolios beating current Sharpe",
    concepts: "Subquery comparison, ORDER BY",
    sql: `SELECT *
FROM optimizer_portfolios
WHERE sharpe > (
  SELECT sharpe FROM optimizer_portfolios WHERE portfolio_id = 'Current'
)
ORDER BY sharpe DESC;`
  },
  {
    workbook: "Quant Analytics (practice)",
    difficulty: "intermediate",
    title: "Average claim amount by policy type",
    concepts: "GROUP BY, AVG, insurance reporting",
    sql: `SELECT policy_type, AVG(claim_amount) AS avg_claim
FROM claims_data
GROUP BY policy_type
ORDER BY avg_claim DESC;`
  },
  {
    workbook: "Quant Analytics (practice)",
    difficulty: "intermediate",
    title: "Highest OPS by team",
    concepts: "GROUP BY, MAX, sports analytics",
    sql: `SELECT team, MAX(ops) AS top_ops
FROM baseball_analytics
GROUP BY team
ORDER BY top_ops DESC;`
  },
  {
    workbook: "Real World Data (practice)",
    difficulty: "intermediate",
    title: "Default rate by sector",
    concepts: "CASE WHEN, AVG, credit risk reporting",
    sql: `SELECT sector,
       AVG(CASE WHEN defaulted = 'Yes' THEN 1.0 ELSE 0 END) AS default_rate
FROM credit_risk_data
GROUP BY sector
ORDER BY default_rate DESC;`
  },
  {
    workbook: "Real World Data (practice)",
    difficulty: "hard",
    title: "Rank portfolios by risk-adjusted return",
    concepts: "RANK(), window function, Sharpe ranking",
    sql: `SELECT month, portfolio_return, sharpe_ratio,
       RANK() OVER (ORDER BY sharpe_ratio DESC) AS sharpe_rank
FROM portfolio_returns;`
  },
  {
    workbook: "Real World Data (practice)",
    difficulty: "hard",
    title: "Fraud claims by region",
    concepts: "WHERE, GROUP BY, COUNT, fraud detection",
    sql: `SELECT region, COUNT(*) AS fraud_count
FROM insurance_claims
WHERE fraud_flag = 'Yes'
GROUP BY region
ORDER BY fraud_count DESC;`
  },
  {
    workbook: "Quant Analytics (joins)",
    difficulty: "intermediate",
    title: "Claims joined with reserve analysis by policy type",
    concepts: "INNER JOIN, GROUP BY, AVG",
    sql: `SELECT c.policy_type,
       AVG(c.claim_amount) AS avg_claim,
       AVG(c.reserve_amount) AS avg_reserve,
       AVG(c.reserve_amount - c.claim_amount) AS avg_reserve_gap
FROM claims_data c
GROUP BY c.policy_type
ORDER BY avg_reserve_gap DESC;`
  },
  {
    workbook: "Real World Data (joins)",
    difficulty: "hard",
    title: "Credit risk joined with sector default summary",
    concepts: "JOIN, GROUP BY, conditional aggregation",
    sql: `SELECT c.sector,
       COUNT(*) AS companies,
       AVG(c.credit_score) AS avg_credit_score,
       AVG(CASE WHEN c.defaulted = 'Yes' THEN 1.0 ELSE 0 END) AS default_rate
FROM credit_risk_data c
GROUP BY c.sector
HAVING COUNT(*) >= 5
ORDER BY default_rate DESC;`
  },
  {
    workbook: "Investment Portfolio (joins)",
    difficulty: "hard",
    title: "Monthly returns joined with risk metrics by ticker",
    concepts: "JOIN, multi-table analysis, risk context",
    sql: `SELECT r.month,
       rm.ticker,
       rm.asset_type,
       rm.sharpe_ratio,
       rm.annual_volatility
FROM risk_metrics rm
CROSS JOIN (
  SELECT DISTINCT month FROM monthly_returns
) r
ORDER BY rm.sharpe_ratio DESC, r.month;`
  },
  {
    workbook: "AI Evaluator (joins)",
    difficulty: "advanced",
    title: "Model performance joined with cost efficiency",
    concepts: "JOIN, aggregation, quality-to-cost analysis",
    sql: `SELECT e.model_name,
       e.prompt_category,
       AVG(e.overall_rating) AS avg_rating,
       AVG(e.cost_usd) AS avg_cost,
       AVG(e.latency_seconds) AS avg_latency,
       AVG(e.overall_rating) / NULLIF(AVG(e.cost_usd), 0) AS quality_per_dollar
FROM evaluation_data e
GROUP BY e.model_name, e.prompt_category
ORDER BY quality_per_dollar DESC;`
  },
  {
    workbook: "Supabase Suite Schema",
    difficulty: "advanced",
    title: "Cross-app activity joined with resume items",
    concepts: "LEFT JOIN, user_id FK, platform analytics",
    sql: `SELECT e.app,
       COUNT(e.id) AS event_count,
       COUNT(DISTINCT r.item_key) AS resume_items,
       MAX(e.timestamp) AS last_activity
FROM suite_activity_events e
LEFT JOIN suite_resume_items r
  ON e.app = r.app AND e.user_id = r.user_id
GROUP BY e.app
ORDER BY event_count DESC;`
  }
];

const PIVOT_EXERCISES = [
  { workbook: "Investment Portfolio", exercise: "Capital split across asset classes", rows: "Asset Type", values: "SUM Dollar Allocation" },
  { workbook: "Investment Portfolio", exercise: "Best risk-adjusted performance by asset type", rows: "Asset Type", values: "AVERAGE Sharpe Ratio" },
  { workbook: "Investment Portfolio", exercise: "Portfolio vs SPY monthly returns", rows: "Month", values: "Portfolio_Return, Market_Return_SPY" },
  { workbook: "Investment Portfolio", exercise: "Monte Carlo outcome distribution", rows: "Ending Value Buckets", values: "COUNT Simulation_ID" },
  { workbook: "Investment Portfolio", exercise: "Efficient frontier candidates", rows: "Portfolio_ID", values: "Return, Volatility, Sharpe" },
  { workbook: "Quant Analytics", exercise: "Total claim amount by policy type", rows: "Policy Type", values: "SUM Claim Amount" },
  { workbook: "Quant Analytics", exercise: "Average claim by risk level", rows: "Risk Level", values: "AVERAGE Claim Amount" },
  { workbook: "Quant Analytics", exercise: "Claims by state and status", rows: "State", columns: "Claim Status", values: "COUNT" },
  { workbook: "Quant Analytics", exercise: "Average OPS by team", rows: "Team", values: "AVERAGE OPS" },
  { workbook: "Quant Analytics", exercise: "HR totals by age group", rows: "Age Group", values: "SUM HR" }
];

const SQL_SKILLS = [
  { skill: "Aggregations", examples: ["AVG", "COUNT", "SUM", "MIN/MAX", "GROUP BY"] },
  { skill: "Filtering", examples: ["WHERE", "IN", "HAVING", "CASE WHEN filters"] },
  { skill: "Joins", examples: ["Implicit via subqueries", "Cross-table portfolio comparisons", "FK relationships in Supabase schema"] },
  { skill: "Window Functions", examples: ["RANK() OVER", "PARTITION BY", "Time-series ranking"] },
  { skill: "Subqueries", examples: ["Portfolio volatility threshold", "Current Sharpe comparison", "Global average benchmark"] },
  { skill: "Conditional Logic", examples: ["CASE WHEN rate calculations", "Bucketing", "Positive/negative month counts"] },
  { skill: "Time Aggregation", examples: ["DATE_TRUNC monthly trends", "Monthly return analysis"] },
  { skill: "Business Reporting", examples: ["Hallucination rates", "Default rates", "Downside probability", "Fraud by region"] }
];

const EXCEL_SKILLS = [
  { skill: "Pivot Tables", examples: ["10 investment exercises", "8 quant analytics exercises", "Cross-tab state/status"] },
  { skill: "Dashboard KPIs", examples: ["AI evaluator dashboard", "Investment analyst dashboard", "Claims/OPS KPIs"] },
  { skill: "Financial Modeling", examples: ["Sharpe ratio", "Monte Carlo percentiles", "Efficient frontier", "Correlation matrices"] },
  { skill: "Data Analysis", examples: ["150-row evaluation dataset", "300 insurance claims", "200 credit risk companies"] },
  { skill: "Chart Storytelling", examples: ["Allocation bar/pie", "Return vs benchmark line", "Risk-return scatter", "Monte Carlo histogram"] },
  { skill: "Distribution Practice", examples: ["Normal, Poisson, Exponential, Gamma, Weibull, Beta"] }
];

function renderQueries() {
  const container = document.getElementById('sql-queries');
  if (!container) return;

  container.innerHTML = SQL_QUERIES.map(q => `
    <div class="query-block">
      <div class="query-header">
        <h4>${q.title}</h4>
        <span>
          <span class="difficulty diff-${q.difficulty}">${q.difficulty}</span>
          <span style="color:var(--muted);font-size:0.8rem;margin-left:0.5rem;">${q.workbook}</span>
        </span>
      </div>
      <div class="query-body">
        <pre><code>${q.sql}</code></pre>
        <div class="concepts"><strong>Concepts:</strong> ${q.concepts}</div>
      </div>
    </div>
  `).join('');
}

function renderSkillsMatrix() {
  const sqlContainer = document.getElementById('sql-skills-matrix');
  const excelContainer = document.getElementById('excel-skills-matrix');

  if (sqlContainer) {
    sqlContainer.innerHTML = SQL_SKILLS.map(s => `
      <div class="skill-card">
        <h4>${s.skill}</h4>
        <ul>${s.examples.map(e => `<li>${e}</li>`).join('')}</ul>
      </div>
    `).join('');
  }

  if (excelContainer) {
    excelContainer.innerHTML = EXCEL_SKILLS.map(s => `
      <div class="skill-card">
        <h4>${s.skill}</h4>
        <ul>${s.examples.map(e => `<li>${e}</li>`).join('')}</ul>
      </div>
    `).join('');
  }
}

function renderPivotExercises() {
  const container = document.getElementById('pivot-exercises');
  if (!container) return;

  container.innerHTML = `<div class="card-grid">${PIVOT_EXERCISES.map(p => `
    <div class="project-card">
      <h3>${p.exercise}</h3>
      <div class="status">${p.workbook}</div>
      <div class="tech-tags">
        <span class="tech-tag">Rows: ${p.rows}</span>
        ${p.columns ? `<span class="tech-tag">Columns: ${p.columns}</span>` : ''}
        <span class="tech-tag">Values: ${p.values}</span>
      </div>
    </div>
  `).join('')}</div>`;
}

document.addEventListener('DOMContentLoaded', () => {
  renderQueries();
  renderSkillsMatrix();
  renderPivotExercises();
});
