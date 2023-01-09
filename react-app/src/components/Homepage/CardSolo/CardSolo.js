import styles from "./CardSolo.module.css";

export default function CardSolo({ product, heading }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>{heading}</div>
                <div className={styles.grid}>
                    <div className={styles.tile}>
                        <img className={styles.image} alt="" src={product?.preview_image} />
                        <div className={styles.title}>{product?.title}</div>
                    </div>
                </div>
            </div>
        </div>
    );
}
