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
import Header from "./Header/Header";
import Line from "./Line/Line";

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
        <Header numItems={numItems} />
        <div className={styles.wrapperWrapper}>
            <div className={styles.wrapper}>
                <div className={styles.content}>
                    <ShippingAddress showAddressSelector={showAddressSelector} setShowAddressSelector={setShowAddressSelector} addresses={addresses} addressIdx={addressIdx} setAddressIdx={setAddressIdx} onAddAddress={onAddAddress} />
                    <Line />
                    <PaymentMethod />
                    <Line />
                    <ReviewItemsAndShipping addresses={addresses} onPlaceOrder={onPlaceOrder} total={total} productDetails={productDetails} cartItems={cartItems} productIds={productIds} />
                </div>
                <OrderSummary addresses={addresses} onPlaceOrder={onPlaceOrder} numItems={numItems} subtotal={subtotal} taxes={taxes} total={total} />
            </div>
        </div>
    </>;
}
