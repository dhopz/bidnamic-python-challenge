from common.base import session
import xlsxwriter
import os

base_path = os.path.abspath(__file__ + "/../../../")
# insight_path = f"{base_path}/data/insights/"

def data_alias():
    data = session.execute("SELECT * FROM insight_alias").all()
    # Create the workbook
    workbook = xlsxwriter.Workbook(
        f"{base_path}/data/insights/alias_query.xlsx"
    )
    # Add a new worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_column(1,1,80)
    worksheet.set_column("C:F", 20)

    worksheet.add_table(
        "B3:F13",
        {
            "data": data,
            "columns": [
                {"header": "alias"},
                {"header": "search_term"},
                {"header": "total_cost"},
                {"header": "total_convesion_value"},
                {"header": "roas"},                
            ],
        },
    )
    workbook.close()

def data_structure_value():
    data = session.execute("SELECT * FROM insight_structure_value").all()
    # Create the workbook
    workbook = xlsxwriter.Workbook(
        f"{base_path}/data/insights/structure_value_query.xlsx"
    )
    # Add a new worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_column("B:F", 20)

    worksheet.add_table(
        "B3:F13",
        {
            "data": data,
            "columns": [
                {"header": "structure_value"},
                {"header": "search_term"},
                {"header": "total_cost"},
                {"header": "total_convesion_value"},
                {"header": "roas"},                
            ],
        },
    )
    workbook.close()


def main():
    print(f"[Export] Alias query sent to {base_path}/data/insights/alias_query.xlsx")
    data_alias()
    print("[Export] Complete")
    print(f"[Export] Structure Value query sent to {base_path}/data/insights/structure_value_query.xlsx")
    data_structure_value()
    print("[Export] Complete")

