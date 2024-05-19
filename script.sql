create table category
(
    category_name varchar(128)                       not null,
    id            int auto_increment
        primary key,
    created_at    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    modified_at   datetime                           null comment '更新时间',
    constraint category_name
        unique (category_name)
);

create index ix_category_id
    on category (id);

create table product
(
    product_name varchar(128)                       not null,
    price        float                              not null,
    quantity     int                                not null,
    description  varchar(128)                       null,
    category_id  int                                not null,
    id           int auto_increment
        primary key,
    created_at   datetime default CURRENT_TIMESTAMP null comment '创建时间',
    modified_at  datetime                           null comment '更新时间',
    constraint product_name
        unique (product_name),
    constraint product_ibfk_1
        foreign key (category_id) references category (id)
);

create index category_id
    on product (category_id);

create index ix_product_id
    on product (id);

create table user
(
    user_name   varchar(128)                       not null,
    pwd         varchar(128)                       not null,
    email       varchar(128)                       null,
    last_login  datetime default CURRENT_TIMESTAMP not null,
    id          int auto_increment
        primary key,
    created_at  datetime default CURRENT_TIMESTAMP null comment '创建时间',
    modified_at datetime                           null comment '更新时间',
    constraint email
        unique (email),
    constraint user_name
        unique (user_name)
);

create table cart
(
    user_id     int                                                  not null,
    id          int auto_increment
        primary key,
    created_at  datetime default CURRENT_TIMESTAMP                   null comment '创建时间',
    modified_at datetime                                             null comment '更新时间',
    status      enum ('ACTIVE', 'CHECKED_OUT', 'ABANDONED', 'SAVED') null,
    constraint user_id_2
        unique (user_id),
    constraint cart_ibfk_1
        foreign key (user_id) references user (id)
);

create index ix_cart_id
    on cart (id);

create index user_id
    on cart (user_id);

create table cart_item
(
    cart_id       int                                null,
    product_id    int                                null,
    quantity      int                                not null,
    price_at_time float                              not null,
    id            int auto_increment
        primary key,
    created_at    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    modified_at   datetime                           null comment '更新时间',
    constraint cart_item_ibfk_1
        foreign key (cart_id) references cart (id),
    constraint cart_item_ibfk_2
        foreign key (product_id) references product (id)
);

create index cart_id
    on cart_item (cart_id);

create index ix_cart_item_id
    on cart_item (id);

create index product_id
    on cart_item (product_id);

create table `order`
(
    user_id     int                                              not null,
    product_id  int                                              not null,
    status      enum ('PAID', 'REFUND', 'DELIVERED', 'RECEIVED') null,
    id          int auto_increment
        primary key,
    created_at  datetime default CURRENT_TIMESTAMP               null comment '创建时间',
    modified_at datetime                                         null comment '更新时间',
    constraint order_ibfk_1
        foreign key (user_id) references user (id),
    constraint order_ibfk_2
        foreign key (product_id) references product (id)
);

create index ix_order_id
    on `order` (id);

create index product_id
    on `order` (product_id);

create index user_id
    on `order` (user_id);

create table order_item
(
    order_id      int                                null,
    product_id    int                                null,
    quantity      int                                not null,
    price_at_time float                              not null,
    id            int auto_increment
        primary key,
    created_at    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    modified_at   datetime                           null comment '更新时间',
    constraint order_item_ibfk_1
        foreign key (order_id) references `order` (id),
    constraint order_item_ibfk_2
        foreign key (product_id) references product (id)
);

create index ix_order_item_id
    on order_item (id);

create index order_id
    on order_item (order_id);

create index product_id
    on order_item (product_id);

create index ix_user_id
    on user (id);


