import { useSelector } from 'react-redux';
import { Navigate } from 'react-router-dom';

export default function Protected({ children }) {
    const user = useSelector(state => state.session.user);
    if (!user) return <Navigate to={`/signin?source=${window.location.pathname + window.location.search}`} replace />;
    return children;
}
