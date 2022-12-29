import styles from "./Price.module.css";

export default function Price({ product }) {
    const price = parseFloat(product.price).toFixed(2);
    const [wholePrice, fractionPrice] = price.split(".");
    return (<div className={styles.wrapper}>
        <div className={styles.symbol}>$</div>
        <div className={styles.whole}>{wholePrice}</div>
        <div className={styles.fraction}>{fractionPrice}</div>
    </div>);
}
