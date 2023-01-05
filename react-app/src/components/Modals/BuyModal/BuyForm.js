import styles from './BuyForm.module.css';
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from 'react-router-dom';
import { setBuyModal } from "../../../store/ui";
import { postOrder } from '../../../store/purchases';

export default function BuyForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { productId, quantity } = useSelector(state => state.ui.buyModal);
    const addresses = useSelector(state => Object.values(state.addresses));
    const address = `${addresses[0].fullname}\n${addresses[0].address.toUpperCase()}\n${addresses[0].city.toUpperCase()}, ${addresses[0].state.toUpperCase()} ${addresses[0].zipcode.toUpperCase()}\n${addresses[0].region}`;

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
        <form className={styles.deleteForm} onSubmit={handleSubmit}>
            <button className={styles.cancel} onClick={() => dispatch(setBuyModal(false))}>x</button>
            <h1>Are you sure you want to order this product?</h1>
            <button className={styles.deleteFormButton} type="submit">Order product</button>
        </form >
    );
}
