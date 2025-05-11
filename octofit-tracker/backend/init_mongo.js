// Initialize the MongoDB database and collections
const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri);

async function initializeDatabase() {
    try {
        await client.connect();
        const db = client.db('octofit_db');

        // Create collections
        await db.createCollection('users');
        await db.createCollection('teams');
        await db.createCollection('activity');
        await db.createCollection('leaderboard');
        await db.createCollection('workouts');

        // Ensure unique email for users
        await db.collection('users').createIndex({ email: 1 }, { unique: true });

        console.log('Database and collections initialized successfully.');
    } catch (error) {
        console.error('Error initializing database:', error);
    } finally {
        await client.close();
    }
}

initializeDatabase();