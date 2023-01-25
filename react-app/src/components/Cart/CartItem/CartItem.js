import styles from "./CartItem.module.css";

import { NavLink } from "react-router-dom";

export default function CartItem({ product, quantity }) {
    if (!product) return;
    return <>
        <div className={styles.wrapper}>
            <div className={styles.left}>
                <NavLink to={`/listing/${product.id}`}><img className={styles.image} src={product.preview_image} alt="" /></NavLink>
                <div className={styles.middle}>
                    <div>
                        <div className={styles.title}><NavLink className={styles.title} to={`/listing/${product.id}`} >{product.title}</NavLink></div>
                        <div className={styles.inStock}>In Stock</div>
                        <div className={styles.shippedFrom}>Shipped from: {product.seller.fullname}</div>
                        <div className={styles.row}>
                            <div className={styles.quantity}>{quantity}</div>
                            <div className={styles.verticalBar} />
                            <div className={styles.delete}>Delete</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.price}>${parseFloat(product.price * quantity).toFixed(2)}</div>
        </div>
        <div className={styles.line}></div>
    </>;
}
