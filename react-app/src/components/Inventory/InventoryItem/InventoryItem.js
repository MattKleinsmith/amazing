import styles from "./InventoryItem.module.css";

export default function InventoryItem({ product }) {
    return (
        <div className={styles.wrapper}>
            <img className={styles.image} src={product.preview_image} alt={product.title} />
            <div className={styles.title}>{product.title}</div>
            <div>
                <div>{product.created_at}</div>
                <div>{product.updated_at}</div>
            </div>
            <div>{product.price}</div>
            <button className={styles.edit}>Edit</button>
            <button className={styles.edit}>Delete</button>
        </div>
    );
}
