# MiniCRM Database Design

# Planned tables

-clients
-cars
-orders
-services
-order_services

## clients

Purpose:
-Przechowuje dane klientów salonu detailingowego.

Fields:
-id
-first_name
-last_name
-phone_number
-email
-note

## cars

Purpose:
-Przechowuje dane samochodów klientów.

Fields:
-id
-client_id
-mark
-model
-generation
-production_year
-license_plate
-color
-vin
-note

Relationship:
-client_id wskazuje na clients.id
-Jeden klient może posiadać wiele samochodów

## orders

Purpose:
-Przechowuje zlecenia wykonywane dla samochodów klientów.

Fields:
-id
-car_id
-order_number
-status
-received_date
-planned_pickup_date
-note

Relationship:
-car_id wskazuje na cars.id
-Jeden samochód może posiadać wiele zleceń

## services

Purpose:
-Przechowuje usługi oferowane przez studio detailingowe

Fields:
-id
-name
-price

## order_services

Purpose:
-Łączy zlecenia z usługami

Fields:
-order_id
-service_id

Relationship:
-order_id wskazuje na orders.id
-service_id wskazuje na services.id
-Jedno zlecenie może zawierać wiele usług
-Jedna usługa może występować w wielu zleceniach