import styles from "./OrderSummary.module.css";

import { useState } from "react";
import { NavLink } from "react-router-dom";

export default function OrderSummary({ addresses, onPlaceOrder, numItems, subtotal, taxes, total }) {
    const [showTerms1, setShowTerms1] = useState(false);
    const [showTerms2, setShowTerms2] = useState(false);
    return <div>
        <div className={styles.subtotalPane}>
            <div className={`${styles.proceed} noselect`} onClick={onPlaceOrder}>{addresses.length > 0 ? "Place your order" : "Add an address"}</div>
            <div className={styles.terms}>By placing your order, you agree to Amazing's <NavLink onClick={() => setShowTerms1(true)} className={styles.link}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setShowTerms2(true)} className={styles.link}> Just Kidding Notice</NavLink>.</div>
            {showTerms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
            {showTerms2 && <div className={styles.jokeTerms2}>Verily, there are no terms.</div>}
            <div className={styles.line2} />

            <div className={`${styles.stepHeader} ${styles.orderSummaryHeading}`}>Order Summary</div>

            <div className={styles.row}>
                <div>Item{numItems > 1 && "s"} ({numItems}):</div>
                <div>${parseFloat(subtotal).toFixed(2)}</div>
            </div>

            <div className={styles.row}>
                <div>Shipping & handling:</div>
                <div>$0.00</div>
            </div>

            <div className={styles.row}>
                <div />
                <div className={styles.line3} />
            </div>

            <div className={styles.row}>
                <div>Total before tax:</div>
                <div>${parseFloat(subtotal).toFixed(2)}</div>
            </div>

            <div className={styles.row}>
                <div>Estimated tax to be collected:</div>
                <div>${parseFloat(taxes).toFixed(2)}</div>
            </div>

            <div className={styles.line2} />
            <div className={styles.totalBottom2}>
                <div>Order total:</div>
                <div>${parseFloat(total).toFixed(2)}</div>
            </div>
        </div>
    </div>
}
