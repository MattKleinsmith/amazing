import styles from "./Cart.module.css";


import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from "react";
import { NavLink, useNavigate } from "react-router-dom";

import CartItem from "./CartItem/CartItem";
import { getProductDetails } from "../../store/productDetails";

export default function Cart() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const cartItems = useSelector(state => state.cartItems);
    const productDetails = useSelector(state => state.productDetails);

    const productIds = Object.keys(cartItems);

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

    const onProceed = async () => {
        navigate(`/checkout`);
    };

    const numItems = productIds.reduce((sum, productId) => sum += cartItems[productId], 0);
    const subtotal = productIds.reduce((sum, productId) => sum += productDetails[productId]?.price * cartItems[productId], 0);

    return <div className={styles.wrapper}>
        <div className={styles.content}>
            <div className={styles.heading}>Shopping Cart</div>
            <div className={styles.priceLabel}>Price</div>
            <div className={styles.line} />
            {productIds.map((productId, i) => <CartItem key={i} product={productDetails[productId]} quantity={cartItems[productId]} />)}
            <div className={`${styles.subtotal} ${styles.mtNegative}`}><span className={styles.subtotalLabel}>Subtotal ({numItems} item{numItems > 1 && "s"}):</span> ${parseFloat(subtotal).toFixed(2)}</div>
        </div>
        <div className={styles.subtotalPane}>
            <div className={styles.subtotal}><span className={styles.subtotalLabel}>Subtotal ({numItems} item{numItems > 1 && "s"}):</span> ${parseFloat(subtotal).toFixed(2)}</div>
            <div className={`${styles.proceed} noselect`} onClick={onProceed}>Proceeed to checkout</div>
        </div>
    </div>;
}
