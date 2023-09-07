def get_data_from_mongo():
    import pymongo
    from pymongo import *
    import pandas as pd

    # Replace with your MongoDB Cloud connection URI
    mongodb_uri = "mongodb+srv://shaikhnaved70:MongoNaved123@nvcluster.kojdtgr.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(mongodb_uri)

    db = client.get_database("mydata")

    # Access a collection within the database
    collection = db.get_collection("mycollection")

    # Fetch data as JSON document  s
    cursor = collection.find({})
    data = list(cursor)

    # Set options to display more rows and columns
    # pd.set_option('display.max_columns', None)  # Display all columns
    # pd.set_option('display.max_rows', None)     # Display all rows

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)
    # print(df)

    # Define a function to format the column headings
    def format_columns(df):
        for col in df.columns:
            new_col = col.lower()
            new_col = new_col.replace("_", "")
            new_col = new_col.replace(" ", "_")
    #         print(new_col)
            df = df.rename(columns={col: new_col})
        return df
    #apply function to change format of data
    df = format_columns(df)

    df.to_csv('C:/Users/Admin/OneDrive/Desktop/output.csv')
    
get_data_from_mongo()
