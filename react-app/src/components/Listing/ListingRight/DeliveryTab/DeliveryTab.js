import styles from "./DeliveryTab.module.css";

import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import Price from "../../../Price/Price";
import Quantity from "../Quantity/Quantity";
import { postOrder } from "../../../../store/purchases"
import { useNavigate } from 'react-router-dom';

export default function DeliveryTab({ product }) {
    const [quantity, setQuantity] = useState(1);
    const addresses = useSelector(state => Object.values(state.addresses));
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onBuyNow = async () => {
        if (addresses.length === 0) {
            navigate(`/addresses/add?productId=${product.id}&quantity=${quantity}`);
        }
        else {
            const address = `${addresses[0].fullname}\n${addresses[0].address.toUpperCase()}\n${addresses[0].city.toUpperCase()}, ${addresses[0].state.toUpperCase()} ${addresses[0].zipcode.toUpperCase()}\n${addresses[0].region}`;
            const cart = { [product.id]: quantity };
            try {
                await dispatch(postOrder({ address, cart }));
                navigate("/order-confirmation");
            } catch (e) {
                console.log("onBuyNow failed:", e);
            }
        }
    }

    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "long", day: "numeric" });

    return (<div className={styles.wrapper}>
        <div className={styles.price}>
            <Price product={product} />
            <div className={styles.count}>(${parseFloat(product.price).toFixed(2)} / Count)</div>
        </div>
        <div className={`prime ${styles.prime}`} />
        <div className={styles.freeReturns}>FREE Returns</div>
        <div className={styles.delivery}>FREE delivery <span className={styles.date}>{deliveryDate}.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
        <div className={styles.address}></div>
        <div className={styles.inStock}>In Stock.</div>
        <Quantity quantity={quantity} setQuantity={setQuantity} />
        <div className={styles.addToCart}>Add to Cart</div>
        <div className={styles.buyNow} onClick={onBuyNow}>Buy Now</div>
        <div className={styles.secure}>
            <div className={styles.secureIconWrapper}>
                <img src="/images/secure.png" alt="Secure icon" height="15px" />
            </div>
            <div className={styles.secureText}>
                Secure transaction
            </div>
        </div>
        <div className={styles.details}>
            <div>
                <div className={styles.detailsLabel}>Ships from</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Sold by</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Packaging</div><div className={styles.detailsText}>Shows what's inside.</div>
            </div>
        </div>
    </div>);
}
