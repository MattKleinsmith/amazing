import styles from "./OrderConfirmation.module.css";

import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { useEffect } from "react";

import { getProductDetails } from "../../store/productDetails";

export default function OrderConfirmation() {
    const order = useSelector(state => state.orders)[0];
    const purchase = order.purchases[0]
    const addressParts = order.address.split('\n');

    const dispatch = useDispatch();
    const product = useSelector(state => state.productDetails)[purchase.product_id];

    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "short", day: "numeric" });

    useEffect(() => {
        dispatch(getProductDetails(purchase.product_id));
    }, [dispatch, purchase]);

    if (!product) return;

    return (
        <div className={styles.outerWrapper}>
            <div className={styles.wrapper}>
                <div className={styles.content}>
                    <div className={styles.innerContent}>
                        <div className={styles.top}>
                            <div className={styles.checkmark} />
                            <div className={styles.thanks}>Order placed, thanks!</div>
                        </div>

                        <div className={styles.confirm}>Confirmation will be shown on <NavLink to="/orders">your orders page</NavLink>.</div>

                        <div><span className={styles.shipping}>Shipping to {addressParts[0]}</span>, {addressParts[1]}, {addressParts[2]}, {addressParts[3]}</div>

                        <div className={styles.line} />

                        <div className={styles.deliveryRow}>
                            <div>
                                <div className={styles.date}>{deliveryDate}</div>
                                <div>Estimated delivery</div>
                            </div>
                            <img className={styles.image} src={product.preview_image} alt="preview" />
                        </div>
                    </div>
                </div>
            </div>
            <NavLink to="/" className={styles.continue}>Continue shopping</NavLink>
        </div>
    );
}
