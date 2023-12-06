# Project Cs50

**YouTube Link:** [Project Demo](https://youtu.be/GibxA8psj10)

I want to create an app using Flask, HTML, CSS, and JavaScript to handle the warehouse of a small activity, such as a construction company. My software app aims to manage the raw materials purchased by the company, upload them to the database, and send them to construction sites for use.
This app could be useful because a lots of small company have not a systems to handle data of raw_materials and sometimes they can lost them, or they can't remember if they have the special raw materials or not.
Using this app they can know this informations save money and not reorder materials that they already has in warehouse. 

## Register Sheet

This is the first page of the app, where the user must register with their name, password, and confirm the password. There's also a check to ensure the password and confirm password match. Possible errors:

1. If the name is already registered, the system will prompt the user to change it.

## Log In

The log-in page is simple. After logging in, users are redirected to the homepage, where they can choose the right path to manage the warehouse.

## Homepage

The homepage greets the user and asks them about two macro paths:

1. **Operative Actions:** Choose options to upload raw materials to the main database or allocate materials to different construction sites.

2. **Visualization Actions:** Visualize different SQL tables called database, history, and split.

## Upload Page

In the upload section, there are four input folders to fill:

1. **Barcode:** Enter 8 digits stored in the database as a barcode associated with materials from suppliers.
2. **Materials:** Enter the name of materials (e.g., cables, bricks, etc.).
3. **Quantities:** Enter the quantities of these materials.
4. **Price:** Enter the price at which you purchased these materials from suppliers. **Note:** The price folder is of float type, so use a dot (.) and NOT a COMMA.

## Database Page

In the database section, you can see raw materials uploaded, including barcode, materials, total quantities, average price, total value, and time of the latest upload. There is also an option to download the CSV database.

## History Page

This page displays all upload transactions of materials, including:

- Name of the operator who uploaded the materials.
- Barcode.
- Materials.
- Quantities.
- Price.
- Total value.
- Time of upload.

## Allocation Page

This page is used to split materials from the company's database to different construction sites. Input folders include barcode, quantities, markup percentage, and the selection of the construction site.

## Split Page

This page displays orders by construction site, including:

- User who sent the materials.
- Barcode.
- Materials.
- Quantities.
- Price to sell.
- Total value.
- Construction site.
- Time of the split transaction.

You can also download CSV using the "Scarica CVS" button, allowing users to handle the data using Excel.
