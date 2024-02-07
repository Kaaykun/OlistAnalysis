# PROJECT IS A WORK IN PROGRESS:

## Olist Data

The Olist dataset consists of information (customers, reviews, products etc..) on 100k orders from the [Olist Store](http://www.olist.com/).

9 csvs (~120mb) are available and can be [downloaded here](https://www.kaggle.com/olistbr/brazilian-ecommerce). We recommend placing them in the `data/csv` folder.

- <a href="#data_model">**Data Model**</a>
- <a href="#olist_customers_dataset">**olist_customers_dataset**</a>
- <a href="#olist_geolocation_dataset">**olist_geolocation_dataset**</a>
- <a href="#olist_order_items_dataset">**olist_order_items_dataset**</a>
- <a href="#olist_order_payments_dataset">**olist_order_payments_dataset**</a>
- <a href="#olist_order_reviews_dataset">**olist_order_reviews_dataset**</a>
- <a href="#olist_orders_dataset">**olist_orders_dataset**</a>
- <a href="#olist_products_dataset">**olist_products_dataset**</a>
- <a href="#olist_sellers_dataset">**olist_sellers_dataset**</a>
- <a href="#product_category_name_translation">**product_category_name_translation**</a>

### Data Model

The schema below represents each dataset and which key to use to join them:

<div id="data_model">

<img src='../img/data_model_olist.png' width='700'>

<div id="olist_customers_dataset">

### olist_customers_dataset

This dataset has information about the customer and their location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.

- `customer_id`: key to the orders dataset. Each order has a unique customer_id.
- `customer_unique_id`: unique identifier of a customer.
- `customer_zip_code_prefix`: first five digits of customer zip code
- `customer_city`: customer city name
- `customer_state`: customer state

<div id="olist_customers_dataset">

### olist_geolocation_dataset

This dataset has information about Brazilian zip codes and lat/lng coordinates. Use it to plot maps and find distances between sellers and customers.

- `geolocation_zip_code_prefix`: first 5 digits of zip code
- `geolocation_lat`: latitude
- `geolocation_lng`: longitude
- `geolocation_city`: city name
- `geolocation_state`: state

<div id="olist_order_items_dataset">

### olist_order_items_dataset

This dataset includes data about the items purchased within each order.

⚠️ If 3 items are purchased in an order, the dataset will display one row per item. If the same product is bought twice, 2 rows will be displayed.

- `order_id`: order unique identifier
- `order_item_id`: sequential number identifying number of items included in the same order.
- `product_id`: product unique identifier
- `seller_id`: seller unique identifier
- `shipping_limit_date`: shows the seller shipping limit date for handling the order over to the logistic partner.
- `price`: item price
- `freight_value`: item freight value (if an order has more than one item the freight value is split between items)

<div id="olist_order_payments_dataset">

### olist_order_payments_dataset

This dataset includes data about order payment options.

- `order_id`: unique identifier of an order.
- `payment_sequential`: a customer may pay for an order with more than one payment method. If they do, a sequence will be created to accommodate all payments.
- `payment_type`: method of payment chosen by the customer.
- `payment_installments`: number of installments chosen by the customer.
- `payment_value`: transaction value.

<div id="olist_order_reviews_dataset">

### olist_order_reviews_dataset

This dataset includes data about the reviews made by a customer.

After a customer purchases the product from the Olist Store, a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where they can leave a note for the purchase experience and write some comments.

- `review_id`: unique review identifier
- `order_id`: unique order identifier
- `review_score`: score ranging from 1 to 5 given by the customer on a satisfaction survey.
- `review_comment_title`: title from the review left by the customer, in Portuguese.
- `review_comment_message`: message from the review left by the customer, in Portuguese.
- `review_creation_date`: shows the date in which the satisfaction survey was sent to the customer.
- `review_answer_timestamp`: shows the satisfaction survey response timestamp.

<div id="olist_orders_dataset">

### olist_orders_dataset

This is the core dataset. For each order, you can find all other information.

- `order_id`: unique identifier of the order.
- `customer_id`: key to the customer dataset. Each order has a unique customer_id.
- `order_status`: reference to the order status (delivered, shipped, etc).
- `order_purchase_timestamp`: shows the purchase timestamp.
- `order_approved_at`: shows the payment approval timestamp.
- `order_delivered_carrier_date`: shows the order posting timestamp, i.e. when it was handed to the logistic partner.
- `order_delivered_customer_date`: shows the actual order delivery date to the customer.
- `order_estimated_delivery_date`: shows the estimated delivery date that was informed to the customer at the time of purchase.

<div id="olist_products_dataset">

### olist_products_dataset

This dataset includes data about the products sold by Olist.

- `product_id`: unique product identifier
- `product_category_name`: root category of product, in Portuguese.
- `product_name_length`: number of characters extracted from the product name.
- `product_description_length`: number of characters extracted from the product description.
- `product_photos_qty`: number of product published photos
- `product_weight_g`: product weight measured in grams.
- `product_length_cm`: product length measured in centimeters.
- `product_height_cm`: product height measured in centimeters.
- `product_width_cm`: product width measured in centimeters.

<div id="olist_sellers_dataset">

### olist_sellers_dataset

This dataset includes data about the sellers that fulfilled orders made at Olist. Use it to find the seller location and to identify which seller fulfilled each product.

- `seller_id`: seller unique identifier
- `seller_zip_code_prefix`: first 5 digits of seller zip code
- `seller_city`: seller city name
- `seller_state`: seller state

<div id="product_category_name_translation">

### product_category_name_translation

Translates the product_category_name to English.

- `product_category_name`: category name in Portuguese
- `product_category_name_english`: category name in English



# Python script README

## Olist Classes

This folder contains Olist Classes that handle the logic of data cleaning for our project.

For example, the below returns data as a Python dictionary using the `get_data` method from the `Olist` class:

```python
from olist.data import Olist
olist = Olist()
data = olist.get_data()
```

### Data

```python
from olist.data import Olist
```

Main methods:

- `get_data`: returns all Olist datasets as DataFrames within a Python dict.

### Order

```python
from olist.order import Order
```

Main method: 
- `get_training_data`: returns a DataFrame with: 
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
from olist.seller import Seller
```

Main method:
- `get_training_data`: returns a DataFrame with:
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
from olist.product import Product
```

Main method:
- `get_training_data`: returns a DataFrame with 
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

### Utils

Utility functions to help during the project.

```python
from olist.utils import *
```

- `haversine_distance(lat1, lng1, lat2, lng2)`: computes distance (in km) between two pairs of (lat, lng) [See Formula](https://en.wikipedia.org/wiki/Haversine_formula)
- `text_scatterplot(df, x, y)`: for a Dataframe `df`, creates a scatterplot with `x` and `y`. The index of `df` is the text label.
- `return_significative_coef(model)`: from a `model` as a statsmodels object, returns significant coefficients.
- `plot_kde_plot(df, variable, dimension)`: plots a side by side kdeplot from DataFrame `df` for `variable`, split by `dimension`.

