import styles from "./Checkout.module.css";


import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";

import CartItem from "./CartItem/CartItem";
import { getProductDetails } from "../../store/productDetails";
import { postOrder } from "../../store/orders";

export default function Checkout() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [showTerms1, setShowTerms1] = useState(false);
    const [showTerms2, setShowTerms2] = useState(false);

    const cartItems = useSelector(state => state.cartItems);
    const productDetails = useSelector(state => state.productDetails);
    const addresses = useSelector(state => Object.values(state.addresses));

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

    const onPlaceOrder = async () => {
        if (addresses.length === 0) {
            // Display Add Address modal
        }
        else {
            try {
                await dispatch(postOrder({ address: addresses[0], cartItems }));
                navigate("/order-confirmation");
            } catch (e) {
                console.log("Order failed:", e);
            }
        }
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
            <div className={`${styles.proceed} noselect`} onClick={onPlaceOrder}>Place your order</div>
            <div className={styles.terms}>By continuing, you agree to Amazing's <NavLink onClick={() => setShowTerms1(true)}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setShowTerms2(true)}> Just Kidding Notice</NavLink>.</div>
            {showTerms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
            {showTerms2 && <div className={styles.jokeTerms2}>Verily, there are no terms.</div>}
        </div>
    </div>;
}
