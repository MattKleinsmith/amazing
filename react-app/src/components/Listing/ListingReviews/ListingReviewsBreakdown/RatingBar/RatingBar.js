import styles from "./RatingBar.module.css"

import { useEffect, useRef } from "react";

export default function RatingBar({ percents, rating }) {
    const ref = useRef();

    console.log("percents[rating]", percents[rating], rating);

    useEffect(() => {
        const classes = {
            5: styles.ratingBarAnimate5,
            4: styles.ratingBarAnimate4,
            3: styles.ratingBarAnimate3,
            2: styles.ratingBarAnimate2,
            1: styles.ratingBarAnimate1
        }

        function playAnimation(entries, observer) {
            entries.forEach(entry => {
                if (entry.intersectionRatio > .2) {
                    ref.current?.style.setProperty(`--width${rating}`, `calc(${percents[rating]}% + ${percents[rating] === 100 ? 2 : 0}px)`);
                    ref.current?.classList.add(classes[rating]);

                    if (percents[rating] === 100) ref.current?.classList.add(styles.curveEnd);
                    else ref.current?.classList.remove(styles.curveEnd);
                }
            });
        }

        const observer = new IntersectionObserver(playAnimation,
            {
                root: null,
                rootMargin: '0px',
                threshold: .2
            });

        if (ref.current) observer.observe(ref.current);
    }, [ref, percents, rating])

    if (isNaN(percents[rating])) return;

    return (
        <div className={styles.wrapper}>
            <div className={styles.starText}>{rating} star</div>
            <div className={styles.ratingBar}><div ref={ref} className={styles.ratingBarFill} /></div>
            <div className={styles.percentText}>{parseFloat(percents[rating]).toFixed(0)}%</div>
        </div>
    );
}
