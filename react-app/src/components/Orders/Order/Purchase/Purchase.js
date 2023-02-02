import styles from "./Purchase.module.css";

import { useDispatch, useSelector } from "react-redux";
import { NavLink, useNavigate } from "react-router-dom";

import { setBuyModal } from "../../../../store/ui";

export default function Purchase({ purchase, isLast, productDetails }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const product = productDetails[purchase.product_id];
    const addresses = useSelector(state => Object.values(state.addresses));

    if (!product) return;

    const onBuyAgain = async () => {
        if (addresses.length === 0) {
            navigate(`/addresses/add?productId=${product.id}&quantity=${1}`);
        }
        else {
            dispatch(setBuyModal(true, product.id, 1));
        }
    }

    return (
        <>
            <div className={styles.bottom}>
                <div>
                    <div className={styles.status}>Not yet shipped</div>
                    <div className={styles.product}>
                        <NavLink to={`/listing/${product.id}`}><img className={styles.previewImage} src={product.preview_image} alt={purchase.order_id} /></NavLink>
                        {purchase.quantity > 1 && <div className={styles.quantity}>{purchase.quantity}</div>}
                        <div>
                            <NavLink to={`/listing/${product.id}`} className={styles.title}>{product.title}</NavLink>
                            <div className={styles.buttonsRow}>
                                <div className={styles.buyItAgain}>
                                    <div className={styles.buyItAgainIcon} />
                                    <div className={styles.buyItAgainText} onClick={onBuyAgain}>Buy it again</div>
                                </div>
                                <NavLink to={`/listing/${product.id}`} className={styles.viewYourItem}>View your item</NavLink>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div className={styles.reviewButton} onClick={() => navigate(`/reviews/${product.id}`)}>{product.is_reviewed_by_current_user ? "Edit" : "Write a"} product review</div>
                </div>
            </div>
            {!isLast && <div className={styles.line} />}
        </>
    );
}
