#include "stdafx.h"
#include "AR.h"


CAR::CAR()
{
	m_attack = 0.05;
	m_release = 0.05;
	m_duration = 0.5;
}


CAR::~CAR()
{
}

void CAR::Start()
{
	m_source->SetSampleRate(GetSampleRate());
	m_source->Start();
	m_time = 0;

}

bool CAR::Generate()
{
	m_source->Generate();

	double gain;
	double actualDuration = m_duration * 0.5;

	if (m_time < m_attack)
	{
		gain = m_time / m_attack;
	}
	else if (m_time > (actualDuration - m_release) )
	{
		gain = 1 - (m_time - m_release) / (actualDuration - m_release);
	}
	else
	{
		gain = 1;
	}

	m_frame[0] = m_source->Frame(0) * gain;
	m_frame[1] = m_source->Frame(1) * gain;

	m_time += GetSamplePeriod();

	return m_time < (actualDuration);
}
