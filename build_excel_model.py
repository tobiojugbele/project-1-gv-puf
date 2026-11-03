import os
import xlsxwriter

def generate_excel_model():
    print("🚀 Project 1: Engineering Excel Actuarial Companion Model...")
    wb = xlsxwriter.Workbook('p1_actuarial_model.xlsx')
    
    # Labeled Assumptions sheet block
    ws_as = wb.add_worksheet('Assumptions')
    ws_as.write('A1', 'Actuarial Projection Assumptions Matrix')
    ws_as.write('A3', 'Stated Baseline Cost Trend Growth Rate')
    ws_as.write('B3', 0.045)  # 4.5% Baseline Trend Assumption Source: EPA Core PUF
    ws_as.write('A4', 'Actuarial Credibility Parameter (k)')
    ws_as.write('B4', 50)
    ws_as.write('A5', 'Scenario Selection Switch (0=Base, 1=High)')
    ws_as.write('B5', 0)
    
    # Trend Projection sheet block
    ws_pr = wb.add_worksheet('Trend Projection')
    ws_pr.write('A1', 'Projection Year')
    ws_pr.write('B1', 'Calculated Pure Premium Baseline')
    ws_pr.write('C1', 'Credibility Weight (Z)')
    
    years = [2024, 2025, 2026, 2027, 2028]
    base_cost = 5000.00
    for idx, year in enumerate(years):
        row = idx + 1
        ws_pr.write(row, 0, year)
        ws_pr.write(row, 1, base_cost * ((1 + 0.045) ** idx))
        ws_pr.write(row, 2, 100 / (100 + 50))
        
    wb.close()
    print("✅ Actuarial companion workbook compiled cleanly: p1_actuarial_model.xlsx")

if __name__ == "__main__":
    generate_excel_model()
