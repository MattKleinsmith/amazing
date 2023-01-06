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
            <NavLink to={`/listing/${product.id}`}><img className={styles.image} src={product.preview_image} alt={product.title} /></NavLink>
            <NavLink to={`/listing/${product.id}`} className={styles.title}>{product.title}</NavLink>
            <div>
                <div>{createdAt}</div>
                <div>{updatedAt}</div>
            </div>
            <div className={styles.price}>{parseFloat(product.price).toFixed(2)}</div>
            <NavLink to={`/inventory/${product.id}`} className={styles.edit}>Edit</NavLink>
            <div onClick={onClickDelete} className={styles.delete}>Delete</div>
        </div>
    );
}
