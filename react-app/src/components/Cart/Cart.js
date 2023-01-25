import styles from "./Cart.module.css";

import { getProductDetails } from "../../store/productDetails";

import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from "react";
import { NavLink } from "react-router-dom";

import CartItem from "./CartItem/CartItem";

export default function Cart() {
    const dispatch = useDispatch();
    const cartItems = useSelector(state => state.cartItems);
    const productIds = Object.keys(cartItems);
    const productDetails = useSelector(state => state.productDetails);

    useEffect(() => {
        productIds.forEach(productId => dispatch(getProductDetails(productId)))
        // eslint-disable-next-line
    }, [dispatch, cartItems]);

    if (productIds.length === 0)
        return <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>Your Amazing Cart is empty.</div>
                <NavLink to="/" className={styles.continue}>Continue shopping</NavLink>
            </div>
        </div>;

    return <div className={styles.wrapper}>
        <div className={styles.content}>
            <div className={styles.heading}>Shopping Cart</div>
            <div className={styles.priceLabel}>Price</div>
            <div className={styles.line}></div>
            {productIds.map((productId, i) => <CartItem key={i} product={productDetails[productId]} quantity={cartItems[productId]} />)}
        </div>
    </div>;
}
