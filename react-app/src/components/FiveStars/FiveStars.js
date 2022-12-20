import styles from "./FiveStars.module.css";

export default function FiveStars({ rating, isBlack }) {
    if (isNaN(Number(rating))) return;
    const fullStarNum = Math.floor(rating);
    const partialStar = rating % 1;
    const lastClass = partialStar > 0.5 ? "" : "-half";
    return (<div className={styles.wrapper}>
        {[...Array(fullStarNum)].map((_, i) => <i key={i} className={`fa-solid fa-star ${styles.icon} ${isBlack ? styles.black : ""}`} />)}
        {partialStar !== 0 && <i className={`fa-solid fa-star${lastClass} ${styles.icon} ${isBlack ? styles.black : ""}`} />}
    </div>);
}
