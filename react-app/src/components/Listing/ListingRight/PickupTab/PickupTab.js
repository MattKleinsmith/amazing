import styles from "./PickupTab.module.css";

import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";

import Quantity from "../Quantity/Quantity";
import { setBuyModal } from "../../../../store/ui";

export default function PickupTab({ product }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [quantity, setQuantity] = useState(1);
    const addresses = useSelector(state => Object.values(state.addresses));
    const user = useSelector(state => state.session.user);

    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "long", day: "numeric" });

    const onBuyNow = async () => {
        if (!user) {
            navigate(`/signin?productId=${product.id}&quantity=${quantity}`);
        }
        else if (addresses.length === 0) {
            navigate(`/addresses/add?productId=${product.id}&quantity=${quantity}`);
        }
        else {
            dispatch(setBuyModal(true, product.id, quantity));
        }
    }

    return (<div className={styles.wrapper}>
        <div className={styles.price}>${parseFloat(product.price).toFixed(2)}</div>
        <div className={styles.delivery}>FREE pickup <span className={styles.date}>{deliveryDate}.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
        <div className={styles.hr} />
        <div className={styles.pickUpLabel}>Pick up at:</div>
        <div className={styles.pickUpLocationWrapper}>
            <div className={styles.pickUpLocation}><span className={styles.locker}>Amazing Hub Locker - Track | </span><span className={styles.distance}>0.08 mi</span></div>
        </div>
        <div className={styles.inStock}>In Stock.</div>
        <Quantity quantity={quantity} setQuantity={setQuantity} />
        <div className={styles.buyNow} onClick={onBuyNow}>Buy Now</div>
        <div className={styles.details}>
            <div>
                <div className={styles.detailsLabel}>Ships from</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Sold by</div><div className={styles.detailsText}>Amazing</div>
            </div>
        </div>
    </div>);
}
