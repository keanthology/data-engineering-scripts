%python
 
table_names_df = spark.sql(f"""
select distinct  a.table_name 
from `system`.information_schema.tables as a
where a.table_catalog='datahub' 
and a.table_schema='currents'
and a.table_name is not null
""")
 
# Collect the table names into a list
table_names_list = [row['table_name'] for row in table_names_df.collect()]
 
# Concatenate the table names with a comma
concatenated_table_names = ','.join(table_names_list)
 
# Split the concatenated table names into 10 parts
split_table_names = [concatenated_table_names[i:i + len(concatenated_table_names) // 10] 
                     for i in range(0, len(concatenated_table_names), len(concatenated_table_names) // 10)]
 
# Ensure the last part includes any remaining characters
if len(split_table_names) > 10:
    split_table_names[9] += ''.join(split_table_names[10:])
    split_table_names = split_table_names[:10]
 
# Print the split table names
for part in split_table_names:
    print(part)
