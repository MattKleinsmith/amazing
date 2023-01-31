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
    const quantity = searchParams.get('quantity');
    const productDetails = useSelector(state => state.productDetails);
    const product = productDetails[productId];
    const cartItems = useSelector(state => state.cartItems);
    const productIds = Object.keys(cartItems);
    const subtotal = productIds.reduce((sum, productId) => sum += productDetails[productId]?.price * cartItems[productId], 0);
    const numItems = productIds.reduce((sum, productId) => sum += cartItems[productId], 0);

    useEffect(() => {
        dispatch(getProductDetails(productId));
        productIds.forEach(productId => dispatch(getProductDetails(productId)))
        // eslint-disable-next-line
    }, [dispatch, productId, cartItems]);

    return <div className={styles.wrapper}>

        <div className={styles.left}>
            <div className={styles.leftContent}>
                <Link to={`/listing/${productId}`} style={{ textDecoration: "none", color: "#0F1111" }}><img src={product?.preview_image} className={styles.leftImage} alt="product" />
                    {quantity > 1 && <div className={styles.quantity}>{quantity}</div>}</Link>

                <div className={styles.leftColumn}>
                    <div className={styles.leftHeading}>
                        <div className={styles.checkmark} />
                        <div className={styles.leftHeadingText}>Added to Cart</div>
                    </div>
                    <Link to={`/listing/${productId}`} style={{ textDecoration: "none" }}><div className={styles.productTitle}>{product?.title}</div></Link>
                </div>
            </div>
        </div>

        <div className={styles.right}>
            <div className={styles.rightHeading}>
                <div className={styles.rightHeadingText}>Cart Subtotal:</div>
                <div className={styles.subtotalWrapper}>
                    <span className={styles.dollarSign}>$</span>
                    <span className={styles.dollars}>{~~subtotal}</span>
                    <span className={styles.cents}>{(subtotal % 1 * 100).toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false })}</span>
                </div>
            </div>
            <Link to={`/checkout`} style={{ textDecoration: "none" }}><div className={`${styles.proceed} noselect`}>Proceed to checkout ({numItems} item{numItems > 1 && "s"})</div></Link>
            <Link to={`/cart`} style={{ textDecoration: "none" }}><div className={`${styles.goToCart} noselect`}>Go to Cart</div></Link>
        </div>

    </div>;
}
