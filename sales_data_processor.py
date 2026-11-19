import csv
#CHECKS------------------------------------------------------------------------
def canbe_int(num):
    '''checks if a number can be an integer'''
    if num is None:
        return False
    try:
        num = int(num)
        if num > 0:
            return True
        return False
    except ValueError:
        return False
    
def canbe_float(num):
    '''checks if a number can be an float'''
    if num is None:
        return False
    try:
        num = float(num)
        if num > 0:
            return True
        return False
    except ValueError:
        return False

#FILE HANDLING----------------------------------------------------------------------
def append_errors(error):
    '''appens errors to error log'''
    with open("error-log.txt", "a", encoding="utf-8") as file:
        file.write(f"{error}\n")

def reset_error_file():
    "resets error file.. duh"
    with open("error-log.txt", "w", encoding="utf-8") as file:
        file.write("")
#MAIN FUNCTIONS--------------------------------------------------------------------------
reset_error_file()
def handle_errors():
    '''appends errors to error log'''
    with open("sales.csv", newline="") as file: #reads and validates sales
        reader = csv.DictReader(file)
        for row_num, row in enumerate(reader, start=2):
            customer = row["Customer"].strip()
            if not customer:
                erline = f"Line {row_num} | Invalid name: '{customer}'"
                append_errors(erline)
            item = row["Item"].strip()
            if not item: 
                erline = f"Line {row_num} | Invalid Item: ' ' "    
                append_errors(erline)       
            if not canbe_int(row["Qty"]):
                erline = f"Line {row_num} | Invalid quantity: {row['Qty']} "
                append_errors(erline)
            if not canbe_float(row["Total"]):
                erline = f"Line {row_num} | Invalid total: {row['Total']} "
                append_errors(erline)

def count_rows():
    '''counts rows'''
    with open("error-log.txt", "r", encoding="utf-8") as file:
        line_count = sum(1 for _ in file)

    print(f"Errors: {line_count}")


def show_valid_orders():
    '''prints valid orders to consol'''
    itemcnt = 0
    sub_total = 0
    with open("sales.csv", newline="") as file: #reads and validates sales
        reader = csv.DictReader(file)
        for row_num, row in enumerate(reader, start=2):
            item = row["Item"].strip()
            item_total = row["Total"].strip()
            if canbe_float(item_total):
                float_item_total = float(item_total)
                sub_total += float_item_total
            if item:
                itemcnt += 1
        print(f"sold {itemcnt} items")
        print(f"made ${sub_total:.2f} ")


        
def main():
    print("""
Sales Sales Processing Complete 
------------------------- 
 """)
    handle_errors()
    show_valid_orders()
    count_rows()
    print("Using files 'error-log.txt' and 'sales.csv'")

if __name__ == "__main__":
    main()

#need to add function to write all valid orders to summary csv, sort by alphabetical order using .sort 