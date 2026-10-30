-- QUERY 1: Regional Grouping & Year-over-Year Trend Analysis (Q1/Q2)
SELECT 
    state,
    reporting_year,
    COUNT(*) as total_reporting_facilities
FROM facilities
GROUP BY state, reporting_year;
