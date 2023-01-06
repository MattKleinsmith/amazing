import styles from "./RatingBar.module.css"

import { useRef } from "react";

export default function RatingBar({ percents, rating }) {
    const ref = useRef();
    ref.current?.style.setProperty('--width', `${percents[rating]}%`);

    return (
        <div className={styles.wrapper}>
            <div className={styles.starText}>{rating} star</div>
            <div ref={ref} className={styles.ratingBar}><div className={styles.ratingBarFill} /></div>
            <div className={styles.percentText}>{parseFloat(percents[rating]).toFixed(0)}%</div>
        </div>
    );
}
