import styles from "./ReviewItemsAndShipping.module.css";

import CheckoutItemList from "./CheckoutItemList/CheckoutItemList";
import BottomSummary from "./BottomSummary/BottomSummary";

export default function ReviewItemsAndShipping({ addresses, onPlaceOrder, total, productDetails, cartItems, productIds }) {
    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    let nextDeliveryDate = new Date(deliveryDate);
    nextDeliveryDate.setDate(nextDeliveryDate.getDate() + 1);
    const deliveryDateBig = deliveryDate.toLocaleDateString('en-us', { month: "short", day: "numeric", year: "numeric" });
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "short", day: "numeric" });
    nextDeliveryDate = nextDeliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "short", day: "numeric" });

    return <div className={styles.step}>
        <div className={`${styles.stepHeader} ${styles.stepNumber}`}>3</div>
        <div>

            <div className={`${styles.stepHeader}`}>Review items and shipping</div>

            <CheckoutItemList productDetails={productDetails} cartItems={cartItems} deliveryDateBig={deliveryDateBig} deliveryDate={deliveryDate} productIds={productIds} nextDeliveryDate={nextDeliveryDate} />

            <BottomSummary addresses={addresses} onPlaceOrder={onPlaceOrder} total={total} />

        </div>
    </div>
}
