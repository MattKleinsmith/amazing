import styles from "./PaymentMethod.module.css";

export default function PaymentMethod() {
    return <div className={styles.step}>
        <div className={`${styles.stepHeader} ${styles.stepNumber}`}>2</div>
        <div className={`${styles.stepHeader} ${styles.stepTitle}`}>Payment method</div>
        <div className={`${styles.stepBody}`}>
            <div className={`${styles.creditCard}`}>
                <img src="https://ducksybucket.s3.amazonaws.com/AmazonPrimeRewardsCardArt._CB485937007_.png" alt="credit card" />
                <div>
                    <div>Amazing Prime Rewards Visa Signature Card <span className={styles.endingIn}>ending in DEMO</span></div>
                    <div className={styles.earn}>Earns 5% back</div>
                </div>
            </div>
            <div className={styles.billing}>Billing address: Same as shipping address.</div>
        </div>
    </div>
}
