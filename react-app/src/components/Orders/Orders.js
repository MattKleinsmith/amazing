import styles from "./Orders.module.css";

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { NavLink } from "react-router-dom";

import { getOrders } from "../../store/orders"

import Order from "./Order/Order";
import { useState } from "react";
import { useLocation } from "react-router";
import { getProductsDetails } from "../../store/productDetails";

export default function Orders() {
    const [page, setPage] = useState(1);
    const size = 10;
    const min = (page - 1) * size;
    const max = min + size;
    const allOrders = useSelector(state => state.orders);
    const orders = allOrders.slice(min, max);
    const productDetails = useSelector(state => state.productDetails);

    useLocation();

    const dispatch = useDispatch();

    useEffect(() => {
        async function fetchData() {
            const orders = await dispatch(getOrders());
            const productIds = [];
            orders.forEach(order => order.purchases.forEach(purchase => productIds.push(purchase.product_id)));
            if (productIds.length > 0)
                dispatch(getProductsDetails(productIds));
        }
        fetchData();
    }, [dispatch]);

    const incrementPage = () => {
        if (page * 10 < allOrders.length) setPage(page + 1);
    }

    const decrementPage = () => {
        if (page > 1) setPage(page - 1);
    }

    document.title = "Your Orders";

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>

                <div className={styles.navInfo}>Your Account {">"} <span className={styles.youAreHere}>Your Orders</span></div>

                <div className={styles.bar}>
                    <div className={styles.heading}>Your Orders</div>
                </div>

                <div className={styles.purchases}>
                    {orders.map((order, i) => <Order key={i} order={order} productDetails={productDetails} />)}
                </div>
                {orders.length === 0 &&
                    <div className={styles.emptyWrapper}>
                        <div>You have no orders.</div>
                        <NavLink to="/" className={styles.continue}>Continue shopping</NavLink>
                    </div>
                }

                {allOrders.length > size && <div className={styles.paginationBar}>
                    <div className={`${styles.paginationButton} ${page <= 1 && styles.disabled} ${styles.noselect}`} onClick={decrementPage}>←Previous</div>
                    <div className={`${styles.paginationButton} ${page * 10 >= allOrders.length && styles.disabled} ${styles.noselect}`} onClick={incrementPage}>Next→</div>
                </div>}
            </div>
        </div>
    );
}
