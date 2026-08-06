CREATE TABLE `Products`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Code` VARCHAR(255) NOT NULL,
    `Name` TEXT NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry_date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock_av` INT NOT NULL
);
CREATE TABLE `Invoices`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Invoice_number` INT NOT NULL,
    `Purchace_date` DATE NOT NULL,
    `Buyer_email` VARCHAR(255) NOT NULL,
    `Total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products_per_invoice (Junction Table)`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `FK_Products` INT NOT NULL,
    `FK_Invoices` INT NOT NULL,
    `Quantity` INT NOT NULL,
    `Total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Shopping_car`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer_email` VARCHAR(255) NOT NULL,
    `FK_invoices` INT NOT NULL
);
CREATE TABLE `Products_per_shopping_car (Junction Table)`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `FK_Shopping_car` INT NOT NULL,
    `FK_Product` INT NOT NULL,
    `Quantity` INT NOT NULL,
    `Total_amount` DECIMAL(8, 2) NOT NULL
);
ALTER TABLE
    `Products_per_shopping_car (Junction Table)` ADD CONSTRAINT `products_per_shopping_car (junction table)_fk_shopping_car_foreign` FOREIGN KEY(`FK_Shopping_car`) REFERENCES `Shopping_car`(`id`);
ALTER TABLE
    `Products_per_shopping_car (Junction Table)` ADD CONSTRAINT `products_per_shopping_car (junction table)_fk_product_foreign` FOREIGN KEY(`FK_Product`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Shopping_car` ADD CONSTRAINT `shopping_car_fk_invoices_foreign` FOREIGN KEY(`FK_invoices`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Products_per_invoice (Junction Table)` ADD CONSTRAINT `products_per_invoice (junction table)_fk_invoices_foreign` FOREIGN KEY(`FK_Invoices`) REFERENCES `Invoices`(`id`);
ALTER TABLE
    `Products_per_invoice (Junction Table)` ADD CONSTRAINT `products_per_invoice (junction table)_fk_products_foreign` FOREIGN KEY(`FK_Products`) REFERENCES `Products`(`id`);