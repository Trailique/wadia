


const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// Define Mongoose schema
const ratingSchema = new mongoose.Schema({
  patientName: String,
  doctorId: String,
  rating: Number
});

// Create Mongoose model
const Rating = mongoose.model('Rating', ratingSchema);

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/ServiceNow', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((error) => {
    console.error('Error connecting to MongoDB:', error.message);
  });

// Route to add rating
app.post('/rate-doctor', async (req, res) => {
  const { patientName, doctorId, rating } = req.body;
  if (!patientName || !doctorId || !rating) {
    return res.status(400).send({ message: 'Patient Name, doctor ID, and rating are required' });
  }

  try {
    const existingRating = await Rating.findOne({ patientName, doctorId });
    if (existingRating) {
      return res.status(400).send({ message: 'Patient has already rated this doctor' });
    }

    const newRating = new Rating({ patientName, doctorId, rating });
    await newRating.save();

    res.status(201).send({ message: 'Rating added successfully', rating: newRating });
  } catch (error) {
    console.error('Error adding rating:', error.message);
    res.status(500).send({ message: 'Internal server error' });
  }
});

// Route to get ratings for a doctor
app.get('/rate-doctor/:doctorId', async (req, res) => {
  const { doctorId } = req.params;

  try {
    const doctorRatings = await Rating.find({ doctorId });
    if (!doctorRatings || doctorRatings.length === 0) {
      return res.status(404).send({ message: 'Doctor not found' });
    }
    res.status(200).send(doctorRatings);
  } catch (error) {
    console.error('Error fetching doctor ratings:', error.message);
    res.status(500).send({ message: 'Internal server error' });
  }
});

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
