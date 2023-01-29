import styles from "./CheckoutItem.module.css";

import { NavLink } from "react-router-dom";

import Quantity from "./Quantity/Quantity";

export default function CheckoutItem({ product, quantity }) {
    if (!product) return;
    return <div className={styles.wrapper}>
        <div className={styles.left}>
            <NavLink to={`/listing/${product.id}`}><img className={styles.image} src={product.preview_image} alt="" /></NavLink>
            <div className={styles.middle}>
                <div>
                    <div className={styles.title}><NavLink className={styles.title} to={`/listing/${product.id}`} >{product.title}</NavLink></div>
                    <div className={styles.row}>
                        <div className={styles.price}>${parseFloat(product.price * quantity).toFixed(2)}</div>
                        <div className={styles.primeIcon} />
                    </div>
                    <Quantity productId={product.id} quantity={quantity} isSmall={true} />
                    <div className={styles.shippedFrom}>Sold by: {product.seller?.fullname}</div>
                </div>
            </div>
        </div>
    </div>;
}
