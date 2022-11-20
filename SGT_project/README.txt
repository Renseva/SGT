For a small business, preparing invoices using spreadsheet tables and a text editor
is not a big undertaking, but I wanted to see how it would work if invoices were generated  by a program.

For my project, I created a small fictional database with two tables,
which contain information about clients and orders respectively.

I used Jupyter notebook to write a program that allows to view or export data contained in the database,
add, update or delete records, and generate basic invoice documents.
In retrospective, as such was my first project of this kind, I appear to have set too ambiguous goals for the time I had,
which is reflected in the long TODO list within the code, not entirely uniform style and the application requiring more
user data entry than expected. It also has virtually no error handling, and, since at the time of writing,
I wasn't up to speed with Pandas, relies more on SQL queries than it would otherwise.

However it is rewarding to see it actually works in that direction and would be of use in a small business activity.

If you find something useful in here, feel free to adopt to your needs.

This would not have happened without wonderful Riga TechGirls (LV), Women Go Tech (LT), Accenture Baltics and Valdis S., to whom all big big thanks!

- - - - - - - - - - - - - - - - - - - - 

SGT_project folder contents:

	README.txt
	fictional.db – small database with two tables Clients and Orders
	data_tables_script.txt – SQLite script to populate initial database data (fictional)
	fictlogo.png – fictional logo image
	application.ipynb – Jupyter notebook file, containing the code
	invoice_211028-1_2021-10-28.pdf – example invoice .pdf file

- - - - - - - - - - - - - - - – - - - -

When running the application, you can do the following actions:

	1 view client and order information:
		          1 view client information or export to Excel: an option to view 10 last clients details on screen or export all clients to an Excel file
             	2 search client records: shows all lines from Clients table where a keyword is found (case insensitive)
             	3 view order details or export to Excel: an option to view 5 last orders details on screen or export all orders to an Excel file
             	4 view order list by specific activity: all orders belonging to a specific type of activity are shown on screen
             	5 view order status: view order status for a specific client (searchable by a portion of client's name)
             	6 return to the main menu.

	2 change client or order details:
		          1 change client notes: change existing client notes
            	2 change order details: change some details for an existing order
            	3 add new client data: add a new client record to the database
             	4 remove client details (when changing notes not enough): delete a specific client's record. Only a warning given,
              no other safeguards. Cannot delete if the client has orders associated with them.
             	5 delete an order: as stated
            	6 return to the main menu.

   	3 create invoices for the orders: generate a .pdf invoice document for a specific order
