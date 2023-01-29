import styles from './BuyForm.module.css';
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from 'react-router-dom';
import { setBuyModal } from "../../../store/ui";
import { postOrder } from '../../../store/orders';

export default function BuyForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { productId, quantity } = useSelector(state => state.ui.buyModal);
    const addresses = useSelector(state => Object.values(state.addresses));
    const address = `${addresses[0].fullname}\n${addresses[0].address.toUpperCase()}\n${addresses[0].city.toUpperCase()}, ${addresses[0].state.toUpperCase()} ${addresses[0].zipcode.toUpperCase()}\n${addresses[0].region}`;
    const product = useSelector(state => state.productDetails[productId]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const cart = { [productId]: quantity };
        try {
            await dispatch(postOrder({ address, cart }));
            dispatch(setBuyModal(false));
            navigate("/order-confirmation");
        } catch (e) {
            console.log("Order failed:", e);
        }
    };

    return (
        <form className={styles.wrapper} onSubmit={handleSubmit}>

            <div className={styles.top}>
                <div className={styles.buyNow}>Buy now: {product.title}</div>
                <div className={styles.close} onClick={() => dispatch(setBuyModal(false))} />
            </div>

            <div className={styles.line} />

            <div className={styles.row}>
                <img className={`${styles.image} ${styles.leftColumn}`} src={product.preview_image} alt="product" />
                <div>
                    <div className={styles.arriving}>Arriving: To Be Determined</div>
                    <div className={styles.free}>FREE Prime Delivery</div>
                    <div className={styles.free}>Sold by Amazing</div>
                </div>
            </div>

            <div className={styles.line} />

            <div className={styles.row}>
                <div className={`${styles.leftColumn}`}>Ship to</div>
                <div>
                    <div className={`${styles.fullname} ${styles.text}`}>{addresses[0].fullname}</div>
                    <div className={styles.text}>{`${addresses[0].address.toUpperCase()}, ${addresses[0].city.toUpperCase()}, ${addresses[0].state.toUpperCase()} ${addresses[0].zipcode.toUpperCase()}, ${addresses[0].region}`}</div>
                </div>
            </div>

            <div className={styles.line} />

            <div className={styles.row}>
                <div className={`${styles.leftColumn}`}>Total</div>
                <div>
                    <div className={`${styles.text} ${styles.price} `}>${parseFloat(product.price * quantity).toFixed(2)}</div>
                    <div className={`${styles.taxNote}`}>(doesn't include tax)</div>
                </div>
            </div>

            <div className={styles.line} />

            <div className={styles.bottom}>
                <button className={`${styles.submitButton} noselect`} type="submit">Place your order</button>
            </div>

        </form>
    );
}
