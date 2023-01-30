import styles from "./AddToCartConfirmation.module.css";

import { useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { getProductDetails } from "../../store/productDetails";

import { Link } from "react-router-dom";

export default function AddToCartConfirmation() {
    const dispatch = useDispatch();
    const searchParams = useSearchParams()[0];
    const productId = searchParams.get('productId');
    const product = useSelector(state => state.productDetails)[productId];

    useEffect(() => {
        dispatch(getProductDetails(productId));
    }, [dispatch, productId]);

    return <div className={styles.wrapper}>

        <div className={styles.left}>
            <div className={styles.leftContent}>
                <Link to={`/listing/${productId}`}><img src={product?.preview_image} className={styles.leftImage} alt="product" /></Link>
                <div className={styles.leftColumn}>
                    <div className={styles.leftHeading}>
                        <div className={styles.checkmark} />
                        <div className={styles.leftHeadingText}>Added to Cart</div>
                    </div>
                    <div className={styles.productTitle}>{product?.title}</div>
                </div>
            </div>
        </div>

        <div className={styles.right}>
            <div className={styles.rightHeading}>
                <div className={styles.rightHeadingText}>Cart Subtotal:</div>
                <div className={styles.subtotalWrapper}>
                    <span className={styles.dollarSign}>$</span>
                    <span className={styles.dollars}>{89}</span>
                    <span className={styles.cents}>{49}</span>
                </div>
            </div>
            <div className={styles.proceed}>Proceed to checkout {123}</div>
            <div className={styles.goToCart}>Go to Cart</div>
        </div>

    </div>;
}
