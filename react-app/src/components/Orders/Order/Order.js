import styles from "./Order.module.css";
import Purchase from "./Purchase/Purchase";


export default function Order({ order }) {
    console.log("order", order);
    const createdAt = (new Date(order.created_at)).toLocaleDateString('en-us', { year: "numeric", month: "long", day: "numeric" });;
    const total = order.purchases.reduce((total, purchase) => total += purchase.price * purchase.quantity, 0)

    return (
        // <div>
        //     Order component
        //     {order.map((product, i) => <div key={i}>{product.product_id}</div>)}
        // </div>
        <div className={styles.wrapper}>
            <div className={styles.top}>
                <div className={styles.topLeft}>
                    <div>
                        <div className={styles.label}>ORDER PLACED</div>
                        <div className={styles.value}>{createdAt}</div>
                    </div>
                    <div>
                        <div className={styles.label}>TOTAL</div>
                        <div className={styles.value}>${parseFloat(total).toFixed(2)}</div>
                    </div>
                    <div>
                        <div className={styles.label}>SHIP TO</div>
                        <div className={styles.value}>{order.address.split('\n')[0]}</div>
                    </div>
                </div>
                <div className={styles.label}>
                    ORDER # {order.id}
                </div>
            </div>

            <div>
                {order.purchases.map((purchase, i) => <Purchase key={i} purchase={purchase} isLast={i === order.purchases.length - 1} address={order.address} />)}
            </div>
        </div>
    );
}
