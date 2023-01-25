import styles from "./CartItem.module.css";

export default function CartItem({ product, quantity }) {
    if (!product) return;
    return <div className={styles.wrapper}>
        {product.title}
        {quantity}
    </div>;
}
