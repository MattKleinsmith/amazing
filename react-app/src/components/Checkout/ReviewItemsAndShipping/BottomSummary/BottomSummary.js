import styles from "./BottomSummary.module.css";

import { useState } from "react";
import { NavLink } from "react-router-dom";

export default function BottomSummary({ addresses, onPlaceOrder, total }) {
    const [showTerms1, setShowTerms1] = useState(false);
    const [showTerms2, setShowTerms2] = useState(false);

    return <div className={`${styles.items} ${styles.orderBottom}`}>
        <div className={`${styles.proceed} noselect  ${styles.bottomPlace}`} onClick={onPlaceOrder}>{addresses.length > 0 ? "Place your order" : "Add an address"}</div>
        <div>
            <div className={styles.totalBottom}>Order total: ${parseFloat(total).toFixed(2)}</div>
            <div className={styles.terms}>By placing your order, you agree to Amazing's <NavLink onClick={() => setShowTerms1(true)} className={styles.link}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setShowTerms2(true)} className={styles.link}> Just Kidding Notice</NavLink>.</div>
            {showTerms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
            {showTerms2 && <div className={styles.jokeTerms2}>Verily, there are no terms.</div>}
        </div>
    </div>
}
