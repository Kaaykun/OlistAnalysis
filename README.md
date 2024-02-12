# Olist Analysis

This is a Brazilian ecommerce public dataset of orders made at [Olist Store](https://olist.com/), the largest department store in Brazilian marketplaces.  
Olist connects small businesses from all over Brazil to channels without hassle and with a single contract.  
Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners.

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order.  
Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email, where he can give a note for the purchase experience and write down some comments.

⚠️ This is real commercial data. It has been anonymised, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses. ⚠️

## Goal

The goal of my investigation of this dataset was to answer the question:

**How could Olist increase its profit?** 

## Notebooks

All the steps taken during this project are visible in the [notebooks folder](https://github.com/Kaaykun/OlistAnalysis/tree/master/notebooks). 

Each notebook builds on the previous one and was also used to create the python scripts described later in the README.

## Olist Data

The Olist dataset consists of information (customers, reviews, products etc..) on 100k orders.

9 csvs (~120mb) are available [to downloaded here](https://www.kaggle.com/olistbr/brazilian-ecommerce) and can be found in the [data/csv folder](https://github.com/Kaaykun/OlistAnalysis/tree/master/data/csv).

### Data Model

The schema below represents each dataset and which key to use to join them:

<div id="data_model">

<img src='img/data_model_olist.png' width='700'>

<div id="olist_customers_dataset">

### olist_customers_dataset

This dataset has information about the customer and their location.

- `customer_id`: Key to the orders dataset. Each order has a unique customer_id
- `customer_unique_id`: Unique identifier of a customer
- `customer_zip_code_prefix`: First five digits of customer zip code
- `customer_city`: Customer city name
- `customer_state`: Customer state

<div id="olist_customers_dataset">

### olist_geolocation_dataset

This dataset has information about Brazilian zip codes and lat/lng coordinates.

- `geolocation_zip_code_prefix`: First 5 digits of zip code
- `geolocation_lat`: Latitude
- `geolocation_lng`: Longitude
- `geolocation_city`: City name
- `geolocation_state`: State

<div id="olist_order_items_dataset">

### olist_order_items_dataset

This dataset includes data about the items purchased within each order.

⚠️ If 3 items are purchased in an order, the dataset will display one row per item. If the same product is bought twice, 2 rows will be displayed.

- `order_id`: Order unique identifier
- `order_item_id`: Sequential number identifying number of items included in the same order
- `product_id`: Product unique identifier
- `seller_id`: Seller unique identifier
- `shipping_limit_date`: Shows the seller shipping limit date for handling the order over to the logistic partner
- `price`: Item price
- `freight_value`: Item freight value (if an order has more than one item the freight value is split between items)

<div id="olist_order_payments_dataset">

### olist_order_payments_dataset

This dataset includes data about order payment options.

- `order_id`: Unique identifier of an order
- `payment_sequential`: A customer may pay for an order with more than one payment method. If they do, a sequence will be created to accommodate all payments
- `payment_type`: Method of payment chosen by the customer
- `payment_installments`: Number of installments chosen by the customer
- `payment_value`: Transaction value

<div id="olist_order_reviews_dataset">

### olist_order_reviews_dataset

This dataset includes data about the reviews made by a customer.

- `review_id`: Unique review identifier
- `order_id`: Unique order identifier
- `review_score`: Score ranging from 1 to 5 given by the customer on a satisfaction survey
- `review_comment_title`: Title from the review left by the customer, in Portuguese
- `review_comment_message`: Message from the review left by the customer, in Portuguese
- `review_creation_date`: Shows the date in which the satisfaction survey was sent to the customer
- `review_answer_timestamp`: Shows the satisfaction survey response timestamp

<div id="olist_orders_dataset">

### olist_orders_dataset

This is the core dataset. For each order, you can find all other information.

- `order_id`: Unique identifier of the order
- `customer_id`: Key to the customer dataset. Each order has a unique customer_id
- `order_status`: Reference to the order status (delivered, shipped, etc)
- `order_purchase_timestamp`: Shows the purchase timestamp
- `order_approved_at`: Shows the payment approval timestamp
- `order_delivered_carrier_date`: Shows the order posting timestamp, i.e. when it was handed to the logistic partner
- `order_delivered_customer_date`: Shows the actual order delivery date to the customer
- `order_estimated_delivery_date`: Shows the estimated delivery date that was informed to the customer at the time of purchase

<div id="olist_products_dataset">

### olist_products_dataset

This dataset includes data about the products sold by Olist.

- `product_id`: Unique product identifier
- `product_category_name`: Root category of product, in Portuguese
- `product_name_length`: Number of characters extracted from the product name
- `product_description_length`: Number of characters extracted from the product description
- `product_photos_qty`: Number of product published photos
- `product_weight_g`: Product weight measured in grams
- `product_length_cm`: Product length measured in centimeters
- `product_height_cm`: Product height measured in centimeters
- `product_width_cm`: Product width measured in centimeters

<div id="olist_sellers_dataset">

### olist_sellers_dataset

This dataset includes data about the sellers that fulfilled orders made at Olist. 

- `seller_id`: Seller unique identifier
- `seller_zip_code_prefix`: First 5 digits of seller zip code
- `seller_city`: Seller city name
- `seller_state`: Seller state

<div id="product_category_name_translation">

### product_category_name_translation

Translates the product_category_name to English.

- `product_category_name`: Category name in Portuguese
- `product_category_name_english`: Category name in English

## Olist Classes

The [utils folder](https://github.com/Kaaykun/OlistAnalysis/tree/master/utils) contains Olist Classes that handle the logic of data cleaning for my project.

For example, the below returns data as a Python dictionary using the `get_data` method from the `Olist` class:

```python
from utils.data import Olist
olist_instance = Olist()
data = olist_instance.get_data()
```

### Data

```python
from utils.data import Olist
```

Main methods:

- `get_data`: Returns all Olist datasets as DataFrames within a Python dictionary.

### Order

```python
from utils.order import Order
```

Main method: 
- `get_training_data`: Returns a DataFrame with: 
   - `order_id` (unique)
   - `wait_time`
   - `expected_wait_time`
   - `delay_vs_expected`
   -  `order_status`
   - `dim_is_five_star`
   - `dim_is_one_star`
   - `review_score`
   -  `number_of_products`
   - `number_of_sellers`
   - `price`
   - `freight_value`
   - `distance_seller_customer`

### Seller

```python
from utils.seller import Seller
```

Main method:
- `get_training_data`: Returns a DataFrame with:
   - `seller_id` (unique)
   - `seller_city`
   - `seller_state`
   - `delay_to_carrier`
   - `wait_time`
   - `date_first_sale`
   - `date_last_sale`
   - `months_on_olist`
   - `share_of_one_stars`
   - `share_of_five_stars`
   - `review_score`
   - `n_orders`
   - `quantity`
   - `quantity_per_order`
   - `sales`

### Product

```python
from utils.product import Product
```

Main method:
- `get_training_data`: Returns a DataFrame with 
   - `product_id` (unique)
   - `product_name_length`
   - `product_description_length`
   - `product_photos_qty`
   - `product_weight_g`
   - `product_length_cm`
   - `product_height_cm`
   - `product_width_cm`
   - `category`
   - `wait_time`
   - `price`
   - `share_of_one_stars`
   - `share_of_five_stars`
   - `review_score`
   - `n_orders`
   - `quantity`
   - `sales`

### Utility

Utility functions to help during the project.

```python
from utils.utility import *
```

- `haversine_distance(lat1, lng1, lat2, lng2)`: Computes distance (in km) between two pairs of (lat, lng) [See Formula](https://en.wikipedia.org/wiki/Haversine_formula)
- `text_scatterplot(df, x, y)`: For a Dataframe `df`, creates a scatterplot with `x` and `y`. The index of `df` is the text label.
- `return_significative_coef(model)`: From a `model` as a statsmodels object, returns significant coefficients.
- `plot_kde_plot(df, variable, dimension)`: Plots a side by side kdeplot from DataFrame `df` for `variable`, split by `dimension`.
