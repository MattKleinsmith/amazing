import styles from "./DeliveryTab.module.css";

import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";

import Price from "../../../Price/Price";
import Quantity from "../Quantity/Quantity";
import { setBuyModal } from "../../../../store/ui"
import { NavLink } from "react-router-dom";
import { postCartItem } from "../../../../store/cartItems";

export default function DeliveryTab({ product }) {
    const [quantity, setQuantity] = useState(1);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const addresses = useSelector(state => Object.values(state.addresses));
    const user = useSelector(state => state.session.user);

    const onBuyNow = () => {
        if (!user) {
            navigate(`/signin?productId=${product.id}&quantity=${quantity}&buyNow=true`);
        }
        else if (addresses.length === 0) {
            navigate(`/addresses/add?productId=${product.id}&quantity=${quantity}`);
        }
        else {
            dispatch(setBuyModal(true, product.id, quantity));
        }
    }

    const onAddToCart = async () => {
        if (!user) {
            navigate(`/signin?productId=${product.id}&quantity=${quantity}&cart=true`);
        }
        else {
            await dispatch(postCartItem(product.id, quantity));
            navigate(`/cart-confirmation?productId=${product.id}`);
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
        {user?.id !== product.seller_id && <Quantity quantity={quantity} setQuantity={setQuantity} />}
        {user?.id !== product.seller_id && <div className={`${styles.addToCart} noselect`} onClick={onAddToCart}>Add to Cart</div>}
        {user?.id !== product.seller_id && <div className={`${styles.buyNow} noselect`} onClick={onBuyNow}>Buy Now</div>}
        {user?.id === product.seller_id && <div>You own this product. <NavLink to={`/inventory/${product.id}?source=${window.location.pathname}`}>Click here</NavLink> to edit it.</div>}
        <div className={styles.secure}>
            <div className={styles.secureIconWrapper}>
                <img src="https://d1irxr40exwge2.cloudfront.net/secure.png" alt="Secure icon" height="15px" />
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
