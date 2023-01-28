import styles from "./Checkout.module.css";

import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";

import { getProductDetails } from "../../store/productDetails";
import { postOrder } from "../../store/orders";
import { setAddressModal } from "../../store/ui";
import { clearCart } from "../../store/cartItems";

import OrderSummary from "./OrderSummary/OrderSummary";
import ReviewItemsAndShipping from "./ReviewItemsAndShipping/ReviewItemsAndShipping";
import PaymentMethod from "./PaymentMethod/PaymentMethod";
import ShippingAddress from "./ShippingAddress/ShippingAddress";

export default function Checkout() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [addressIdx, setAddressIdx] = useState(0);
    const [showAddressSelector, setShowAddressSelector] = useState(false);

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
            onAddAddress();
        }
        else {
            try {
                const address = `${addresses[addressIdx].fullname}\n${addresses[addressIdx].address.toUpperCase()}\n${addresses[addressIdx].city.toUpperCase()}, ${addresses[addressIdx].state.toUpperCase()} ${addresses[addressIdx].zipcode.toUpperCase()}\n${addresses[addressIdx].region}`;
                await dispatch(postOrder({ address, cart: cartItems }));
                dispatch(clearCart());
                navigate("/order-confirmation");
            } catch (e) {
                console.log("Order failed:", e);
            }
        }
    };

    const onAddAddress = () => {
        dispatch(setAddressModal(true));
    }

    const numItems = productIds.reduce((sum, productId) => sum += cartItems[productId], 0);
    const subtotal = productIds.reduce((sum, productId) => sum += productDetails[productId]?.price * cartItems[productId], 0);
    const taxRate = 0.08687954888;
    const taxes = subtotal * taxRate;
    const total = subtotal + taxes;

    return <>
        <div className={styles.headerWrapper}>
            <div className={styles.header}>
                <NavLink to="/" className={styles.logo}><img src="https://d1irxr40exwge2.cloudfront.net/logo_black.png" alt="logo_black" /></NavLink>
                <div className={styles.checkout}>Checkout <span className={styles.checkoutItem}>(<NavLink to="/cart" className={styles.checkoutLink}>{numItems} item{numItems > 1 && "s"}</NavLink>)</span></div>
                <div className={styles.secureIconWrapper}>
                    <img src="https://d1irxr40exwge2.cloudfront.net/secure.png" alt="Secure icon" height="20px" />
                </div>
            </div>
        </div>

        <div className={styles.wrapperWrapper}>

            <div className={styles.wrapper}>

                <div className={styles.content}>

                    <ShippingAddress showAddressSelector={showAddressSelector} setShowAddressSelector={setShowAddressSelector} addresses={addresses} addressIdx={addressIdx} setAddressIdx={setAddressIdx} onAddAddress={onAddAddress} />

                    <div className={`${styles.line}`} />

                    <PaymentMethod />

                    <div className={`${styles.line}`} />

                    <ReviewItemsAndShipping addresses={addresses} onPlaceOrder={onPlaceOrder} total={total} productDetails={productDetails} cartItems={cartItems} productIds={productIds} />

                </div>

                <OrderSummary addresses={addresses} onPlaceOrder={onPlaceOrder} numItems={numItems} subtotal={subtotal} taxes={taxes} total={total} />

            </div>

        </div>
    </>;
}
