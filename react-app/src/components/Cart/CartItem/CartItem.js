import styles from "./CartItem.module.css";

export default function CartItem({ product, quantity }) {
    if (!product) return;
    return <>
        <div className={styles.wrapper}>
            <img className={styles.image} src={product.preview_image} alt="" />
            <div className={styles.middle}>
                <div lassName={styles.title}>{product.title}</div>
                <div lassName={styles.quantity}>{quantity}</div>
            </div>
            <div className={styles.price}>${parseFloat(product.price).toFixed(2)}</div>
        </div>
        <div className={styles.line}></div>
    </>;
}
