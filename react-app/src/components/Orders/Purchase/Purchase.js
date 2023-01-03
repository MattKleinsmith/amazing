import styles from "./Purchase.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";

import { getProductDetails } from "../../../store/productDetails";

export default function Purchase({ purchase }) {
    const createdAt = (new Date(purchase.created_at)).toLocaleDateString('en-us', { year: "numeric", month: "long", day: "numeric" });;

    const dispatch = useDispatch();
    const product = useSelector(state => state.productDetails)[purchase.product_id];

    useEffect(() => {
        dispatch(getProductDetails(purchase.product_id));
    }, [dispatch]);

    if (!product) return;

    return (
        <div className={styles.wrapper}>
            <div className={styles.top}>
                <div className={styles.topLeft}>
                    <div>
                        <div className={styles.label}>ORDER PLACED</div>
                        <div className={styles.value}>{createdAt}</div>
                    </div>
                    <div>
                        <div className={styles.label}>TOTAL</div>
                        <div className={styles.value}>${parseFloat(purchase.price * purchase.quantity).toFixed(2)}</div>
                    </div>
                    <div>
                        <div className={styles.label}>SHIP TO</div>
                        <div className={styles.value}>{purchase.address.split('\n')[0]}</div>
                    </div>
                </div>
                <div className={styles.label}>
                    ORDER # {purchase.order_id}
                </div>
            </div>

            <div className={styles.bottom}>
                <div>
                    <div className={styles.status}>Not yet shipped</div>
                    <div className={styles.product}>
                        <NavLink to={`/listing/${product.id}`}><img className={styles.previewImage} src={product.preview_image} alt={purchase.order_id} /></NavLink>
                        <div>
                            <NavLink to={`/listing/${product.id}`} className={styles.title}>{product.title}</NavLink>
                            <div className={styles.buttonsRow}>
                                <div className={styles.buyItAgain}>
                                    <div className={styles.buyItAgainIcon} />
                                    <div className={styles.buyItAgainText}>Buy it again</div>
                                </div>
                                <div className={styles.viewYourItem}>View your item</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div className={styles.reviewButton}>Write a product review</div>
                </div>
            </div>
        </div>
    );
}
