import styles from "./InventoryItem.module.css";

import { useDispatch } from "react-redux";
import { NavLink } from 'react-router-dom';

import { deleteProduct } from '../../../store/products';

export default function InventoryItem({ product }) {
    const dispatch = useDispatch();
    const onClickDelete = () => {
        dispatch(deleteProduct(product.id));
    };

    const createdAt = (new Date(product.created_at)).toLocaleString();
    const updatedAt = (new Date(product.updated_at)).toLocaleString();

    return (
        <div className={styles.wrapper}>
            <img className={styles.image} src={product.preview_image} alt={product.title} />
            <div className={styles.title}>{product.title}</div>
            <div>
                <div>{createdAt}</div>
                <div>{updatedAt}</div>
            </div>
            <div>{product.price}</div>
            <NavLink to={`/inventory/${product.id}`}><button className={styles.edit}>Edit</button></NavLink>
            <button onClick={onClickDelete} className={styles.edit}>Delete</button>
        </div>
    );
}
