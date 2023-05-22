import React, { useState, useEffect } from 'react';
import axios from "axios";
import WeekDaysChart from "./charts/WeekDays";
import TrendChart from "./charts/Trend";
import Card from './Card';
import Table from './Table';

const Dashboard = () => {

    const [data, setData] = useState([]);
    const [daysCatSum, setDaysCatSum] = useState({});
    const [daysStat, setDaysStat] = useState({});
    const [shops, setShops] = useState({});


    useEffect(() => {
        axios.get('/parse/stat')
            .then((response) => {
                const data = response.data
                setData(data);
                setDaysCatSum(data.totalDaysCatSum);                
                setDaysStat(data.days);
                setShops(data.shops);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    function formatNumber(number) {
        return number.toLocaleString('ru-RU', {
            style: 'currency',
            currency: 'RUB',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        });
    }

    return (
        <div className="container mt-3">
            <div className="row g-6 mb-6">
                <Card props={{
                    name: 'Объем рынка', body: (data.totalValue ? formatNumber(data.totalValue) : '. . . '), icon: 'bi bi-box-fill',
                    color: 'success', badge: true, badgeBody: data.valueDiff, badgeText: 'со вчера'
                }} />
                <Card props={{
                    name: 'Продажи за 7 дней', body: (data.curDaysSumCost ? formatNumber(data.curDaysSumCost) : '. . . '), icon: 'bi bi-cart-check',
                    color: 'warning', badge: true, badgeBody: data.prevDaysSumDiff, badgeText: 'с прошлого периода'
                }} />
                <Card props={{
                    name: 'Наибольший спрос сегодня', body: data.bestCatToday, icon: 'bi bi-bookmark-heart',
                    color: 'info', badge: false, badgeText: data.bestCatTodayPercent + '% от общей суммы'
                }} />
                <Card props={{
                    name: 'Средняя цена', body: data.averagePrice + ' ₽', icon: 'bi bi-cash-coin',
                    color: 'primary', badge: true, badgeBody: data.priceDiff, badgeText: 'за сутки'
                }} />
            </div>

            <div className="row mt-4">
                <div className="col-xxl-8 col-lg-8 col-md-12">
                    <div className="rounded shadow p-3">
                        <h4><i className="bi bi-graph-up text-success"> </i>Динамика продаж</h4>
                        {
                            daysStat[0] ? <TrendChart props={daysStat} /> : <p>Загрузка...</p>
                        }
                    </div>
                </div>
                <div className="col-xxl-4 col-lg-4 col-md-12">
                    <div className="rounded shadow p-3">
                        <h4>Статистика за 7 дней</h4>
                        {
                           daysCatSum ? <WeekDaysChart props={daysCatSum} /> : <p>Загрузка...</p>
                        } 
                    </div>
                </div>
            </div>
            <div className="row p-3">
                {
                    shops[0] ? <Table props={shops}/> : <p>Загрузка...</p>
                }
            </div>
        </div>

    );
};

export default Dashboard;
