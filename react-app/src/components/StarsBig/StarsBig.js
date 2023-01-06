import styles from "./StarsBig.module.css";

export default function StarsBig({ rating }) {

    if (isNaN(Number(rating))) return;

    let className = styles.zero;

    if (rating >= 4.8) {
        className = styles.five;
    } else if (rating > 4.1) {
        className = styles.four_half;
    } else if (rating >= 3.8) {
        className = styles.four;
    } else if (rating > 3.1) {
        className = styles.three_half;
    } else if (rating >= 2.8) {
        className = styles.three;
    } else if (rating > 2.1) {
        className = styles.two_half;
    } else if (rating >= 1.8) {
        className = styles.two;
    } else if (rating > 1.1) {
        className = styles.one_half;
    } else if (rating >= 0.8) {
        className = styles.one;
    } else if (rating > 0.1) {
        className = styles.zero_half;
    } else {
        className = styles.zero;
    }

    return <div className={`${styles.stars} ${className}`} />;
}
